<!-- write me a readme for this project. Its an AI virtual assistant (Intelligent Virtual Assistant - IVA) called MusicHub.
    It processes user input using NLP techniques and responds accordingly. It can answer music related questions, and play music.
    It uses ML models to understand the intent behind users input. If the user asks a music related question, it will answer it.
    If the users wants to play music, it will play music. After the IVA understands the user intent, it sends a request to OpenAI API
    for data and YouTube API for music. The machine learning logic is built using python, the API using Flask, and the front end using React.
   
    To train the intent recognition model, run the train_model.py file that is inside the intent_recognition folder. 
    To train the named entity recognition model, run the spacy CLI command "python -m spacy train config_path --o output_path", or in this case:
    "python -m spacy train named_entity_recognition/spacy_config.cfg -o named_entity_recognition/models/mh_ner/v2.0


-->

# MusicHub

MusicHub is an AI virtual assistant that processes user input using NLP techniques and is able to answer to music related questions, and play music. It uses ML models to understand the intent behind users input. If the user asks a music related question, it will answer it. If the users wants to play music, it will play music. After the IVA understands the user intent, it sends a request to OpenAI API for data and YouTube API for music. The machine learning logic is built using python, the API using Flask, and the front end using React.

## Installation

Use the package manager [pip] to install the required packages.

```bash
pip install -r requirements.txt
```

## Training the models

If you want to train the models, the intent recognition model is trained by running the following command inside the intent_recognition folder:
```python
python train_model.py
```
You can change the intent recognition model hyperparameters in the neuralintents.py file or add more intents by editing the intents.json file. The model is a sequential model with 3 dense layers and 2 dropout layers in between. The model is compiled using the SGD optimizer with a learning rate of 0.005, and trained for 50 epochs with a batch size of 5. The model is trained on 80% of the data and validated on 20% of the data. The model is trained to predict the intent of the user input using the following code:
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

        self.hist = self.model.fit(np.array(train_x), np.array(train_y), epochs=50, batch_size=5, verbose=1, validation_data=(np.array(val_x), np.array(val_y)))
```


To train the named entity recognition model, run the spacy CLI command 
```bash
python -m spacy train config_path --o output_path
```
or in this case, run the following command inside the named_entity_recognition folder:
```bash
python -m spacy train spacy_config.cfg -o models/mh_ner/v2.0
```
You can change the named entity recognition model hyperparameters in the spacy_config.cfg file or edit the training data by editing the files inside the music_data folder.
To create examples for model training for all the different entities (songs, albums etc.) like:
    "Play me 'song_name' by 'artist_name'",
    "Hi, I want to listen to 'album_name;",
    etc.
run the following command inside the named_entity_recognition folder:
```bash
python create_training_data.py
```
This will create a training data file called training_data.json and validation_data.json inside the music_data folder, as well as training_data.spacy and validation_data.spacy that the model will use to train and validate. 

## Usage

To run the API, run the app.py.
```python
python app.py
``` 

To run the front end, run the npm start command.
```bash
npm start
```

## Contributing

## License

# MusicHub

