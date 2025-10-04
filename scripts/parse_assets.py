import pandas as pd
import ollama
from config.constants import prompt

def read_excel(file_path):
    """
    Reads data from an Excel file and returns it as a DataFrame.
    """
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def search_excel(data, column_name, search_value):
    """
    Searches for a value in a specific column of the DataFrame.
    """
    if column_name not in data.columns:
        print(f"Error: Column '{column_name}' not found in the Excel file.")
        return None

    # Filter rows where the column contains the search value
    results = data[data[column_name].astype(str).str.contains(search_value, case=False, na=False)]
    return results

import subprocess
import json

def query_llm_with_excel(data, query):
    """
    Uses the Ollama Python API to process a query and search the Excel data.
    """
    try:
        # Convert the DataFrame to a string format for the LLM
        excel_content = data.to_string(index=False)

        full_prompt = f"{prompt}\n\nQuery: {query}\n\nData:\n{excel_content}"

        # ✅ Correct use of Ollama Python API
        response = ollama.chat(
            model='mistral',
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes tabular data."},
                {"role": "user", "content": full_prompt}
            ]
        )

        return response['message']['content']
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return None
