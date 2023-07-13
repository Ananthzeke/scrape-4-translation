### Installation
``` pip install requirements.txt ```
### Evaluation script
``` python scores.py ```
#### About the script
- With the help of evaluate module from Hugging Face loaded ```sacrebleu``` and ```chrf``` metrics to calulate the scores of each model.
- ```scores``` that takes a file path and a metric as input. It extracts the language from the file name, reads the CSV file into a DataFrame, computes the metric score by comparing the predictions column with the references column, and returns the scores along with the language in a DataFrame.
- This  code computes evaluation scores (BLEU and chrF) for translated datasets and saves the scores in separate CSV files.
