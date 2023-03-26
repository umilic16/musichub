import os
import sys
sys.path.append('../')
from helpers.json_functions import load_data, save_data
from typing import Dict, List

def rate_models(folderpath: str) -> dict:
    """
    Returns a dictionary containing performance metrics of all the models found in the folderpath and identifies the 
    best performing model by F-score.

    Args:
        folderpath (str): The path of the directory that contains the model-best directory of each model.

    Returns:
        dict: A dictionary containing the best performing model and all the models found in the folderpath along with their performance metrics.
    """
    data = []
    for folder in os.listdir(folderpath):
        meta = load_data(f'{folderpath}/{folder}/model-best/meta.json')
        if meta is None:
            break
        f_score = meta['performance']['ents_f'] * 100
        precision = meta['performance']['ents_p'] * 100
        recall = meta['performance']['ents_r'] * 100
        value = {'version': folder, 'F-score': f_score, 'precision': precision, 'recall': recall}
        # print(value)
        data.append(value)
    data = sorted(data, key=lambda item: item['F-score'], reverse=True)
    data = [{'version': entry['version'], 'F-score': f'{entry["F-score"]:.2f}%', 'precision': f'{entry["precision"]:.2f}%', 'recall': f'{entry["recall"]:.2f}%'}
              for entry in data]
    result = {}
    result['best'] = data[0]
    result['all-models'] = data
    return result

save_data('models_rating.json', rate_models('models/mh_ner'))
save_data('models_rating_gc.json', rate_models('../google_colab_training/'))
