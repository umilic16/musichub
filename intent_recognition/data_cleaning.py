import json
from helpers.json_functions import load_data, save_data

data = load_data('data/train-v2.0.json')

def filter_json(original_json):
    new_data = []
    for obj in original_json:
        filtered_obj = {'title': obj['title'], 'paragraphs': []}
        for paragraph in obj['paragraphs']:
            filtered_qas = [{'question': qas['question']} for qas in paragraph['qas']]
            filtered_paragraph = {'qas': filtered_qas}
            filtered_obj['paragraphs'].append(filtered_paragraph)
        new_data.append(filtered_obj)
    return new_data

def clean_entries():
    for entry in data:
        # Prompt the user to confirm deletion of current entry
        user_input = input(f"Delete entry with title '{entry['title']}'? (y/n): ")
        if user_input.lower() == "y":
            # Remove the current entry from the data array
            data["data"].remove(entry)
        elif user_input.lower() == 'stop':
            break

def clean_questions():
    for entry in data:
        for qas in entry['paragraphs']:
            for question in qas['qas']:
            # Prompt the user to confirm deletion of current question
                user_input = input(f"Delete question '{question}'? (y/n): ")
                # print(question)
                if user_input.lower() == "y":
                    # Remove the current entry from the data array
                    del question

def reformat_questions():
    result = []
    for entry in data:
        for qas in entry['paragraphs']:
            for question in qas['qas']:
                result.append(question['question'])
    return result

# clean_entries()
# data = filter_json(data)
data = reformat_questions()

# Write the updated data object back to the JSON file
save_data('data/train-v2.0.json', data)


