from transformers import BertTokenizer, BertForSequenceClassification
import torch.optim as optim
import torch
import json

import json

with open('intents.json') as f:
    data = json.load(f)

train_labels = []
train_texts = []
train_values = []

# Prepare the training data
for idx, intent in enumerate(data['intents']):
    train_values.append(intent['tag'])

model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(train_values))
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model.load_state_dict(torch.load('train_gpt_model.pt'))
# Use the fine-tuned model to recognize user intent
def recognize_intent(user_input):
    encoded_input = tokenizer.encode_plus(user_input, return_tensors='pt')
    output = model(**encoded_input)
    predicted_intent = torch.argmax(output.logits)
    return predicted_intent.item()

# Example usage
done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        intent = recognize_intent(message)
        print(train_values[intent])
        # if intent:
        #     print(train_values[intent])

