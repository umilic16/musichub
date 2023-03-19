from neuralintents import GenericAssistant

def request_data():
    print("You triggered request_data")
    # Some action you want to take

def play_music():
    print("You triggered play_music!")
    # Some action you want to take

mappings = {'request_data' : request_data, 'play_music' : play_music}
assistant = GenericAssistant('data/intents.json', intent_methods=mappings ,model_name="test_model")
assistant.load_model()


done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        response = assistant.request(message)
        if response:
            print(response)