import os,re
import pandas as pd
import multiprocessing as mp
from indicnlp.tokenize import sentence_tokenize
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
factory=IndicNormalizerFactory()

def pandas_clean(row,language):
  row=re.sub('<.*?>', '', str(row))
  row=re.sub(r'<a\s+.*?</a>','', row)
  if factory.is_language_supported(language):
    normalizer=factory.get_normalizer(language,remove_nuktas=True)
    row=normalizer.normalize(row)
  row=sentence_tokenize.sentence_split(row,lang=language)
  return row

def preprocess_using_pandas(path):
  en='eng'
  indic_lang=os.path.basename(path).split(".")[0]
  if factory.is_language_supported(indic_lang):
    df=pd.read_csv(path,sep=':=',engine='python',names=[en,indic_lang],dtype='str')
    # filtering the dataframe by no of words in sentence
    df=df[df[en].map(lambda x : len(str(x).split(' '))>3)] 
    # filtering out English senetences from dataframe
    df=df[df[indic_lang].map(lambda sentences : not re.match(r'^[A-Za-z0-9\s\W]+$', str(sentences)) )]
    #cleaning the text
    dff=df[en].map(lambda x : pandas_clean(x,'en')).to_frame()
    dff[indic_lang]=df[indic_lang].map(lambda x : pandas_clean(x,indic_lang))
    #filtering out the tokenized sentences that has not matching lengths

    condition=dff[dff[en].map(lambda x : len(x))!=dff[indic_lang].map(lambda x : len(x))]
    if not condition.empty:
       dff.update(condition.applymap(lambda x :''.join(map(str, x))))
    #flattening the nested lists to single list
    dff=dff.explode(list(dff.columns))
    dff.to_csv(f'processed_dataset/{indic_lang}.csv',index=False)
  return f'language {indic_lang} is not supported'

def using_multiprocessing(dir,num_proc=mp.cpu_count()):
  ds_path=[dir+path for path in os.listdir(dir)]
  if not os.path.exists('processed_dataset'):
      os.mkdir('processed_dataset')
  with mp.Pool(num_proc) as pool:
      pool.map(preprocess_using_pandas,ds_path)

using_multiprocessing('/home/ananth/scrape-4-translation/dataset/')