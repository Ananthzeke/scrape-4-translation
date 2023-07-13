# add fairseq folder to python path
import os
os.environ['PYTHONPATH'] += ":/content/fairseq/"
# sanity check to see if fairseq is installed
from fairseq import checkpoint_utils, distributed_utils, options, tasks, utils
from datasets import load_dataset
from indicTrans.inference.engine import Model

indic2en_model = Model(expdir='../indic-en')
def translate_dataset(path,sentences=100,dir='translated',batch_size=16):
  #supported languages
  INDIC = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]
  indic_lang=os.path.basename(path).split(".")[0]
  if indic_lang in INDIC:
    indic_ds=load_dataset('csv',data_files=[path])
    # filterinig out the sentences with number of words
    indic_ds=indic_ds.filter(lambda x : (len(x['eng'].split())>5) and (len(x['eng'].split())<30))
    # Selecting Sample for inference
    indic_ds=indic_ds['train'].select(range(sentences))
    #inference
    indic_ds=indic_ds.map(
        lambda  x : {'indic_trans_translated':indic2en_model.batch_translate(x[indic_lang],indic_lang, 'en')}
                          ,batched=True,batch_size=batch_size
                          )
    indic_ds.to_csv(f'{dir}/{indic_lang}.csv')
    return f'translated {indic_lang} to eng'
  return f'language not supported{indic_lang}'

dir='/content/indicTrans/scrape-4-translation/processed_dataset/'
ds_path=[dir+path for path in os.listdir(dir)]
dir='translated_dataset'
if not os.path.exists(dir):
    os.mkdir(dir)
for path in ds_path:
  translate_dataset(path,dir)