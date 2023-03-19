import json

# Read the JSON file into a Python object
with open("train-v2.0.json", 'r') as f:
    data = json.load(f)

# Iterate through each entry in the data array
for entry in data["data"]:
    # Prompt the user to confirm deletion of current entry
    user_input = input(f"Delete entry with title '{entry['title']}'? (y/n): ")
    if user_input.lower() == "y":
        # Remove the current entry from the data array
        data["data"].remove(entry)
    elif user_input.lower() == 'stop':
        break

# Write the updated data object back to the JSON file
with open("train-v2.0.json", 'w') as f:
    json.dump(data, f)
