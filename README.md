# MusicHub

readme not finished

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

Code for training the intent recognition model is from [**`neuralintents`**](https://github.com/NeuralNine/neuralintents) library, with small changes. You can change the intent recognition model hyperparameters in the [neuralintents.py](intent_recognition/neuralintents.py#L92-L108) file or add more intents by editing the [intents.json](intent_recognition/data/intents.json) file. The [intents.json](intent_recognition/data/intents.json) file contains tags and patterns for each intent. The tags are the intents that the patterns represent, and the patterns represent different forms of user input. For example:

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
Named entity recognition model is trained using the [**`spaCy`**](https://spacy.io/) library. This model uses spaCy pre-trained word embedding model **en_core_web_lg** during the training process, and if you want to train the named entity recognition model using it you have to download it using this command (there are other pre-trained models that you can use as well [[learn more](https://spacy.io/usage/models)]):
```bash
python -m spacy download en_core_web_lg
```
To change the configuration for named entity recognition model training, you can edit the [spacy_config.cfg](named_entity_recognition/spacy_config.cfg) file.
To train the named entity recognition model, run the spaCy CLI command for training [[learn more](https://spacy.io/api/cli#train)]: 
```bash
python -m spacy train config_path --o output_path
```
or in this case, the last model is trained running the following command inside the named_entity_recognition folder:
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
    
The spacy files will contain the same examples but in a format that the spacy library can use to train the model. To speed up the training process you can generate a file that contains the labels in the data. This helps speed up the training process, since spaCy won’t have to preprocess the data to extract the labels. This can be done by running the following spaCy CLI command [[learn more](https://spacy.io/api/cli#init-labels)]:
```bash
python -m spacy init labels config_path output_path
```
or in this case, the labels are initialized by running the following command inside the named_entity_recognition folder:
```bash
python -m spacy init labels spacy_config.cfg data/ner_labels
```


## Usage

To run the API, run the app.py.
```python
python app.py
``` 

To run the front end, run the npm start command.
```bash
npm start
```
