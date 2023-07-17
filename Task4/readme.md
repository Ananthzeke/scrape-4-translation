### Installation
``` pip install requirements.txt ```
### Hugging Face models Inference scripts
``` python hf_inference.py ```
#### About the scripts
- HF models inferences can be run on either CPU or GPU.
- In ```hf_inference_using_pipeline.py``` that takes a pipeline, file path, model name, number of sentences, directory path for saving the translated dataset, and batch size as inputs. It loads a translation model using the Hugging Face pipeline,here I have used ```mBART 600M```model that retrieves the language from the file name, loads the dataset from the CSV file, filters it based on English sentence length, selects a subset of sentences, performs translation using the pipeline, creates a DataFrame from the translation predictions, creates a Hugging Face Dataset from the DataFrame, concatenates the original dataset with the translated dataset, and saves the translated dataset as a CSV file.
- In ```hf_inference.py``` without the use of pipeline, direct tokenizing and predicting the output and decoding the prediction. This solves the prefix problem with the pipeline.  
- Taken a sample of sentences that has words more than 3 and less than 30  for an inference, GPU is recommended for faster inferences.
