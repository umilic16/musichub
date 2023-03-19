# Step 2: Load the pre-trained models
from transformers import BertTokenizer, BertForSequenceClassification
import torch.optim as optim
import torch
import json
from sklearn.model_selection import train_test_split
import numpy as np

with open('data/intents.json') as f:
    data = json.load(f)

train_labels = []
train_texts = []
train_values = []

# Prepare the training data
for idx, intent in enumerate(data['intents']):
    train_values.append(intent['tag'])
    for pattern in intent['patterns']:
        train_labels.append(idx)
        train_texts.append(pattern)

# for text, label in zip(train_texts, train_labels):
#     print(f'Text: {text}\nLabel: {label}\n')


train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=0.2)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(train_values))

encoded_train_texts = tokenizer(train_texts, padding=True, truncation=True, return_tensors='pt')
train_dataset = torch.utils.data.TensorDataset(encoded_train_texts['input_ids'], encoded_train_texts['attention_mask'], torch.tensor(train_labels))
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=16, shuffle=True)

encoded_val_texts = tokenizer(val_texts, padding=True, truncation=True, return_tensors='pt')
val_dataset = torch.utils.data.TensorDataset(encoded_val_texts['input_ids'], encoded_val_texts['attention_mask'], torch.tensor(val_labels))
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=16, shuffle=True)

# Fine-tune the model on the training data
optimizer = optim.AdamW(model.parameters(), lr=5e-5)
model.train()

for epoch in range(30):
    # Train the model on the training set
    model.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch in train_loader:
        input_ids, attention_mask, labels = batch
        output = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = output.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        train_loss += loss.item() * len(labels)
        predicted = torch.argmax(output.logits, dim=1)
        correct += (predicted == labels).sum().item()
        total += len(labels)

    # Calculate accuracy and loss on the validation set
    model.eval()
    val_loss = 0
    val_correct = 0
    val_total = 0
    with torch.no_grad():
        for batch in val_loader:
            input_ids, attention_mask, labels = batch
            output = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = output.loss

            val_loss += loss.item() * len(labels)
            predicted = torch.argmax(output.logits, dim=1)
            val_correct += (predicted == labels).sum().item()
            val_total += len(labels)

    train_accuracy = correct / total
    train_loss /= len(train_dataset)
    val_accuracy = val_correct / val_total
    val_loss /= len(val_dataset)

    print(f'Epoch {epoch+1}: Train Loss: {train_loss:.4f}, Train Acc: {train_accuracy:.4f}, Val Loss: {val_loss:.4f}, Val Acc: {val_accuracy:.4f}')

torch.save(model.state_dict(), 'models/train_gpt_model.pt')


# Use the fine-tuned model to recognize user intent
def recognize_intent(user_input):
    encoded_input = tokenizer.encode_plus(user_input, return_tensors='pt')
    output = model(**encoded_input)
    predicted_intent = torch.argmax(output.logits)
    return predicted_intent.item()

# Example usage
# user_input = "Can you play a song by Eminem?"
# intent = recognize_intent(user_input)
# print(train_values[intent])
