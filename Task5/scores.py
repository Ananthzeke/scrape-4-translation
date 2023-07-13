import pandas as pd
import evaluate
import os
bleu = evaluate.load('  ')
chrf=evaluate.load('chrf')
def scores(path,metric):
  indic_lang=os.path.basename(path).split(".")[0]
  df=pd.read_csv(path)
  scores=pd.DataFrame([metric.compute(predictions=df[df.columns[0]],references=df[df.columns[-1]])])
  scores['language']=indic_lang
  return scores
def scores_to_csv(model_name,dir='./translated_indic_trans/'):
    bleu_score=pd.concat([scores(dir+path,bleu) for path in os.listdir(dir)]).set_index('language')
    chrf_score=pd.concat([scores(dir+path,chrf) for path in os.listdir(dir)]).set_index('language')
    bleu_score.to_csv(f'{model_name}_bleu_scores.csv')
    chrf_score.to_csv(f'{model_name}_bleu_scores.csv')
scores_to_csv('indic_trans')