### Installation
```pip install requirements.txt```
### Preprocessing script
```python preprocess.py```

#### About the script
- Function ```pandas_clean``` that takes a row and a language as input. It applies various cleaning operations to the row, such as removing HTML tags, normalizing the text using the IndicNormalizerFactory based on the language, and tokenizing the sentences using the sentence_tokenize function from indicnlp.tokenize. The cleaned row is returned.
- Then  ```preprocess_using_pandas``` that takes a file path as input. It extracts the language from the file name, reads the file into a pandas DataFrame using a specified separator, filters the DataFrame based on the number of words in the English sentence, filters out English sentences using a regular expression, applies the pandas_clean function to clean the text in both English and the indicated language, filters out tokenized sentences that have different lengths between English and the indicated language, and finally flattens the nested lists in the DataFrame. The cleaned and processed DataFrame is saved as a CSV file.
- Then used multiprocessing to parallelize the execution of the ```preprocess_using_pandas``` function on the file paths.
