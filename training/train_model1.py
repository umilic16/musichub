from neuralintents import GenericAssistant

assistant = GenericAssistant('data/intents.json', model_name="test_model")
assistant.train_model()
assistant.save_model()

# done = False

# while not done:
#     message = input("Enter a message: ")
#     if message == "STOP":
#         done = True
#     else:
#         response = assistant.request(message)
#         if response:
#             print(response)
