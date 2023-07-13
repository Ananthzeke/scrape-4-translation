### Installation
``` pip install requirements.txt ```
### Scraping script
``` python scrape.py ```
#### About the script
- Defined a function ```fetch_url``` that takes a language, directory, URL, and a replaceable value as input. It sends a GET request to the URL with the language parameter, retrieves the JSON response, flattens the nested JSON structure, and saves the flattened JSON to a file in the specified directory.
- Another function ```matching_json``` that takes two languages, a new directory, and a JSON directory as input. It opens the JSON files for the given languages, loads the data into dictionaries, finds the matching keys between the two dictionaries, and writes the matching keys along with their corresponding values to a new text file in the specified directory.
- Atlast function ```using_threading``` that takes  a list of languages, a directory, and the number of worker threads as input. It creates a thread pool executor with the specified number of workers, creates the output directory if it doesn't exist, and maps the given function to the list of languages using the executor.
- For I/O operations threading and asynchronus are the best.
