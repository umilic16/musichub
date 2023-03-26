import os
import sys
sys.path.append('../')
from helpers.json_functions import load_data, save_data


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
            continue
        performance = meta['performance']
        f_score = performance['ents_f'] * 100
        precision = performance['ents_p'] * 100
        recall = performance['ents_r'] * 100
        tok2vec_loss = performance['tok2vec_loss']
        ner_loss = performance['ner_loss']
        value = {'version': folder, 'F-score': f'{f_score:.2f}%', 'precision': f'{precision:.2f}',
                 'recall': f'{recall:.2f}%', 'tok2vec_loss': f'{tok2vec_loss:.2f}', 'ner_loss': f'{ner_loss:.2f}'}
        # print(value)
        data.append(value)
    data = sorted(data, key=lambda item: item['F-score'], reverse=True)
    # print(data)
    result = {}
    result['best'] = data[0]
    result['all-models'] = data
    return result


save_data('models_rating.json', rate_models('models/mh_ner'))
save_data('models_rating_gc.json', rate_models('../google_colab_training/'))
