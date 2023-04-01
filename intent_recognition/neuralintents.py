from keras.models import load_model
from keras.optimizers import SGD
from keras.layers import Dense, Dropout
from keras import Sequential
from nltk.stem import WordNetLemmatizer
import nltk
import random
import json
import pickle
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

"""
Modified version of neural intents library by NeuralNine, original code available on github:
https://github.com/NeuralNine/neuralintents

"""

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)


class GenericAssistant():

    def __init__(self, intents="", responses="", intent_methods={}, model_name="assistant_model"):
        self.intents = intents
        self.intent_methods = intent_methods
        self.model_name = model_name
        self.responses = responses

        if intents.endswith(".json"):
            self.load_json_intents(intents)

        if responses.endswith(".json"):
            self.load_json_responses(responses)

        self.lemmatizer = WordNetLemmatizer()

    def load_json_intents(self, intents):
        self.intents = json.loads(open(intents).read())

    def load_json_responses(self, responses):
        self.responses = json.loads(open(responses).read())

    def train_model(self):

        self.words = []
        self.classes = []
        documents = []
        ignore_letters = ['!', '?', ',', '.']

        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                word = nltk.word_tokenize(pattern)
                self.words.extend(word)
                documents.append((word, intent['tag']))
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        self.words = [self.lemmatizer.lemmatize(
            w.lower()) for w in self.words if w not in ignore_letters]
        self.words = sorted(list(set(self.words)))

        self.classes = sorted(list(set(self.classes)))

        training = []
        output_empty = [0] * len(self.classes)

        for doc in documents:
            bag = []
            word_patterns = doc[0]
            word_patterns = [self.lemmatizer.lemmatize(
                word.lower()) for word in word_patterns]
            for word in self.words:
                bag.append(1) if word in word_patterns else bag.append(0)

            output_row = list(output_empty)
            output_row[self.classes.index(doc[1])] = 1
            training.append([bag, output_row])

        # random.shuffle(training)
        training = np.array(training, dtype=object)

        x = list(training[:, 0])
        y = list(training[:, 1])

        # Split the data into training and validation sets
        train_x, val_x, train_y, val_y = train_test_split(
            x, y, test_size=0.33, random_state=42)

        self.model = Sequential()
        self.model.add(Dense(256, input_shape=(
            len(train_x[0]),), activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(len(train_y[0]), activation='softmax'))

        sgd = SGD(learning_rate=0.0033, decay=1e-6, momentum=0.9, nesterov=True)
        self.model.compile(loss='categorical_crossentropy',
                           optimizer=sgd, metrics=['accuracy'])

        self.hist = self.model.fit(np.array(train_x), np.array(
            train_y), epochs=300, batch_size=32, verbose=1, validation_data=(np.array(val_x), np.array(val_y)), shuffle=True)
        
        plt.subplot(1, 2, 1)
        plt.plot(self.hist.history['loss'])
        plt.plot(self.hist.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Training', 'Validation'], loc='upper right')
        plt.subplot(1, 2, 2)
        plt.plot(self.hist.history['accuracy'])
        plt.plot(self.hist.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Training', 'Validation'], loc='lower right')
        plt.show()

    def save_model(self, path="models", model_name=None):
        if model_name is None:
            self.model.save(f"{path}/{self.model_name}.h5", self.hist)
            pickle.dump(self.words, open(
                f'{path}/{self.model_name}_words.pkl', 'wb'))
            pickle.dump(self.classes, open(
                f'{path}/{self.model_name}_classes.pkl', 'wb'))
        else:
            self.model.save(f"{path}/{model_name}.h5", self.hist)
            pickle.dump(self.words, open(
                f'{path}/{model_name}_words.pkl', 'wb'))
            pickle.dump(self.classes, open(
                f'{path}/{model_name}_classes.pkl', 'wb'))

    def load_model(self, path, model_name=None):
        if model_name is None:
            self.words = pickle.load(
                open(f'{path}/{self.model_name}_words.pkl', 'rb'))
            self.classes = pickle.load(
                open(f'{path}/{self.model_name}_classes.pkl', 'rb'))
            self.model = load_model(f'{path}/{self.model_name}.h5')
        else:
            self.words = pickle.load(
                open(f'{path}/{model_name}_words.pkl', 'rb'))
            self.classes = pickle.load(
                open(f'{path}/{model_name}_classes.pkl', 'rb'))
            self.model = load_model(f'{path}/{model_name}.h5')

    def _clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(
            word.lower()) for word in sentence_words]
        return sentence_words

    def _bag_of_words(self, sentence, words):
        sentence_words = self._clean_up_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, word in enumerate(words):
                if word == s:
                    bag[i] = 1
        return np.array(bag)

    def _predict_class(self, sentence):
        p = self._bag_of_words(sentence, self.words)
        res = self.model.predict(np.array([p]), verbose=0)[0]
        ERROR_THRESHOLD = 0.51
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append(
                {'intent': self.classes[r[0]], 'probability': str(r[1])})
        return return_list

    def _get_response(self, ints, responses_json):
        try:
            tag = ints[0]['intent']
            list_of_responses = responses_json['intents']
            for i in list_of_responses:
                if i['tag'] == tag:
                    result = random.choice(i['responses'])
                    break
        except IndexError:
            result = "I don't understand!"
        return result

    def request(self, message):
        ints = self._predict_class(message)
        if (ints):
            # print(ints[0]['intent'])
            if ints[0]['intent'] in self.intent_methods.keys():
                return self.intent_methods[ints[0]['intent']](message)
            else:
                return {"type": "data", "data": self._get_response(ints, self.responses)}
