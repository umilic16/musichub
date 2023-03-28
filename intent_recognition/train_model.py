from neuralintents import GenericAssistant

assistant = GenericAssistant(intents = 'data/intents.json', model_name="intent_recognition")
assistant.train_model()
assistant.save_model()