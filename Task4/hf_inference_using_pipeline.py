import torch,os
import pandas as pd
from transformers import pipeline
from datasets import load_dataset,Dataset,concatenate_datasets

#device if GPU is present the inference may run on GPU
device = torch.cuda.current_device() if torch.cuda.is_available() else -1


def hf_inference(pipe,path,model='facebook/nllb-200-distilled-600M',sentences=100,dir='translated_dataset',batch_size=16):
  #loading the translator model with hf pipeline
  pipe=pipeline('translation',model,device=device)
  indic_lang=os.path.basename(path).split(".")[0]
  #loading csv as hugging face datasets
  indic_ds=load_dataset('csv',data_files=[path])
  #filtering out sentences that less than 5 words and more than 30 words
  indic_ds=indic_ds.filter(lambda x : (len(x['eng'].split())>5) and (len(x['eng'].split())<30))
  indic_ds=indic_ds['train'].select(range(sentences))
  predictions=pipe(indic_ds[indic_lang],src_lang=indic_lang, tgt_lang="eng",batch_size=batch_size)
  df=pd.DataFrame(predictions)
  pred=Dataset.from_pandas(df)
  trans_ds=concatenate_datasets([indic_ds,pred],axis=1)
  trans_ds.to_csv(f'{dir}/{indic_lang}.csv')

dir='scrape-4-translation/processed_dataset/'
ds_path=[dir+path for path in os.listdir(dir)]

new_dir='hf_translated_dataset'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
for path in ds_path:
  hf_inference(model,tokenizer,path)