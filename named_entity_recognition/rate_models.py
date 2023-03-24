import os
from helpers.json_functions import load_data, save_data

def rate_models(folderpath):
    data = []
    for folder in os.listdir(folderpath):
        meta = load_data(f'{folderpath}/{folder}/model-best/meta.json')
        f_score = round(meta['performance']['ents_f'] * 100, 2)
        precision = round(meta['performance']['ents_p'] * 100, 2)
        recall = round(meta['performance']['ents_r'] * 100, 2)
        value = {'version': folder, 'F-score': f_score, 'precision': precision, 'recall': recall}
        # print(value)
        data.append(value)
    data = sorted(data, key=lambda item: item['F-score'], reverse=True)
    data = [{'version': entry['version'], 'F-score': f'{entry["F-score"]}%', 'precision': f'{entry["precision"]}%', 'recall': f'{entry["recall"]}%'}
              for entry in data]
    result = {}
    result['best'] = data[0]
    result['all-models'] = data
    return result

save_data('models_rating.json', rate_models('models/mh_ner'))
