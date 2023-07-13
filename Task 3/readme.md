### Installation
```bash install.sh```
### Indic-Trans inference script
```python inference.py```

#### About the script
- The ```translate_dataset``` function takes a file path, number of sentences, directory path, and batch size as inputs. It checks if the language in the file name is supported, loads the dataset from the CSV file, filters it based on English sentence length, selects a subset of sentences, performs batch translation using the model, and saves the translated dataset.
- Iterates over the file paths in the processed datasets directory. For each file, it calls the ```translate_dataset``` function to translate the dataset and saves the translated dataset in the newly created directory.
