from transformers import  AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
import torch,os

device = torch.cuda.current_device() if torch.cuda.is_available() else -1
model_name='facebook/nllb-200-distilled-600M'

# moving seq2seq model to GPU 
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def translator(text,indic_lang,model,tokenizer):
  tokenizer.src_lang=indic_lang
  txt=tokenizer.batch_encode_plus(text,return_tensors='pt',padding=True,truncation=True)
  txt.to(device)
  prediction=model.generate(**txt, forced_bos_token_id=tokenizer.lang_code_to_id['eng_Latn'])
  translation=tokenizer.batch_decode(prediction, skip_special_tokens=True)
  return translation

def hf_inference(model,tokenizer,path,dir='translated_dataset',batch_size=32):
  indic_lang=os.path.basename(path).split(".")[0]
  indic_ds=load_dataset('csv',data_files=[path])
  indic_ds=indic_ds.filter(lambda x : (len(x['eng'].split())>5) and (len(x['eng'].split())<30))
  indic_ds=indic_ds.map(lambda x : {'mBART600M': translator(x[indic_lang],indic_lang,model,tokenizer)},batched=True,batch_size=batch_size)
  indic_ds['train'].to_csv(f'{dir}/{indic_lang}.csv')


dir='scrape-4-translation/processed_dataset/'
ds_path=[dir+path for path in os.listdir(dir)]

new_dir='hf_translated_dataset'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
for path in ds_path:
  hf_inference(model,tokenizer,path)
