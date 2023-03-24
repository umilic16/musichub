import os
import sys
sys.path.append('../')
from helpers.json_functions import load_data, save_data

def rate_models(folderpath):
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
