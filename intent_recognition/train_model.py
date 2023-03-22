from neuralintents import GenericAssistant

assistant = GenericAssistant('data/intents.json', model_name="test_model")
assistant.train_model()
assistant.save_model()