# MusicHub

**MusicHub** is an AI virtual assistant that processes user input using **NLP** (natural language processing) techniques and is able to answer to music related questions, and play music. It uses **machine learning** models to understand the intent behind users input and extract relevant entities. If the user asks a music related question, it will answer it. If the users wants to play music, it will play music. After the IVA understands the user intent, it sends a request to **OpenAI API** for data and **YouTube API** for music. The machine learning logic is built using python, the API using **Flask**, and the front end using **React**.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/latest/installation/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Training the models
### Intent recognition model
The intent recognition model is trained by running the following command inside the intent_recognition folder:
```python
python train_model.py
```
In the [train_model.py](intent_recognition/train_model.py) file, you can change the training data file path, and the model path. After training is done the model is saved in the [models](intent_recognition/models) folder. The

Code for training the intent recognition model is from [**`neuralintents`**](https://github.com/NeuralNine/neuralintents) library, with small changes. You can change the intent recognition model hyperparameters in the [neuralintents.py](intent_recognition/neuralintents.py#L92-L108) file or add more intents by editing the [intents.json](intent_recognition/data/intents.json) file. The model is a sequential model with 3 dense layers and 2 dropout layers in between. The model is compiled using SGD optimizer with learning rate of 0.005, and categorical crossentropy loss function. The model is trained for 100 epochs with batch size of 8. The model is trained on 80% of the data and validated on 20% of the data. In code, that looks like this:

```python
        train_x, val_x, train_y, val_y = train_test_split(x, y, test_size=0.2, random_state=42)

        self.model = Sequential()
        self.model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(len(train_y[0]), activation='softmax'))

        sgd = SGD(learning_rate=0.005, decay=1e-6, momentum=0.9, nesterov=True)
        self.model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

        self.hist = self.model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=8 verbose=1, validation_data=(np.array(val_x), np.array(val_y)))
```

The [intents.json](intent_recognition/data/intents.json) file contains tags and patterns for each intent. The tags are the intents that the patterns represent, and the patterns represent different forms of user input. For example:

    "tag": "request_data",
    "patterns": [
                    "Who is mozzart",
                    "What do you know about Method Man",
                    "Can you tell me more about the life of Freddie Mercury?",
                    "What are some of the biggest hits from Michael Jackson?"
                ]
    "tag": "play_music",
    "patterns": [
                    "Play Michale Jackson Thriller",
                    "I want to listen to 'Stairway to Heaven' by Led Zeppelin.",
                    "Hey Music Hub, gimme some rock",
                    "Can you put on some electronic dance music, please?"
                ]
There are also intents that are not music related, like "greeting", "goodbye", "thanks" etc. The model is trained to recognize these intents as well, and respond accordingly. For these intents the responses are predefined and can be found in [responses.json](intent_recognition/data/responses.json) file.
### Named entity recognition model
Named entity recognition model is trained using the [**`spaCy`**](https://spacy.io/) library. This model uses spaCy pre-trained word embedding model **en_core_web_lg** during the training process, and you can download it using this command:
```bash
python -m spacy download en_core_web_lg
```
To change the named entity recognition model hyperparameters, you can edit the [spacy_config.cfg](named_entity_recognition/spacy_config.cfg) file.
To train the named entity recognition model, run the spacy CLI command 
```bash
python -m spacy train config_path --o output_path
```
or in this case, the last model is trained using following command inside the named_entity_recognition folder:
```bash
python -m spacy train spacy_config.cfg -o models/mh_ner/v2.2
```
 or edit the training data by editing the files inside the [music_data](named_entity_recognition/data/music_data) folder. To create examples for model training run the following command inside the named_entity_recognition folder:
```bash
python create_training_data.py
```
This will create files training_data.json and validation_data.json inside the [data](named_entity_recognition/data) folder, as well as training_data.spacy and validation_data.spacy that the model will use to train and validate. The json files will contain examples for all the different entities (songs, albums etc.) like:

    "Play me song_name by artist_name",
    "Hi, I want to listen to album_name",
    "Play song_name from album_name"

as well as labeled entities for each example. Let's take a look:
    
        {
            "text": "Play me song_name by artist_name",
            "entities": [
                {
                    "start": 8,
                    "end": 17,
                    "label": "SONG"
                },
                {
                    "start": 21,
                    "end": 32,
                    "label": "ARTIST"
                }
            ]
        }
    
The spacy files will contain the same examples but in a format that the spacy library can use to train the model.


## Usage

To run the API, run the app.py.
```python
python app.py
``` 

To run the front end, run the npm start command.
```bash
npm start
```
