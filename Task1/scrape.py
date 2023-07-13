import requests,os,json
from flatten_json import flatten
from itertools import repeat
languages=['en','ta','hi','gu','te','ur','mr','ml','kn','bn','as','pa','or','ne','doi','kok','sd','brx','mai','mni','sat','ks']
from concurrent.futures import ThreadPoolExecutor
def fetch_url(lan,dir,url='https://www.poshantracker.in/locales/en.json?v19',replacable='en'):

    try:
        response=requests.get(url.replace(replacable,lan),timeout=3)
        if response.status_code >= 400:
            raise Exception(f"Unable to scrape URL. Response code: {response.status_code}")
        with open(f'{dir}/{lan}.json','w') as f:
                json.dump(flatten(response.json()),f,indent=4)
    except Timeout:
        print("Request timed out.")
    except Exception as e:
        print(str(e))

# Writes a text file that contains matching keys from the eng.json and indic.json for creating a parallel corpora
def matching_json(lang1,new_dir,lang2='en',json_dir='./dataset_json'):
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    with open(f'{json_dir}/{lang1}.json','r') as file1,open(f'{json_dir}/{lang2}.json','r') as file2:
        in_data=json.load(file1)
        en_data=json.load(file2)
    matching_keys = set(in_data.keys()).intersection(set(en_data.keys()))
    new=[en_data[key].replace('\n','')+' := '+in_data[key].replace('\n','') for key in matching_keys]

    with open(f'{new_dir}/{lang1}.txt','w') as file:
        file.write('\n'.join(new))


def using_threading(function,languages,dir,workers=8):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        if not os.path.exists(dir):
            os.mkdir(dir)
        print(executor.map(function,languages,repeat(dir)))

using_threading(fetch_url,languages,dir='./dataset_json')
using_threading(matching_json,languages,dir='./dataset')
