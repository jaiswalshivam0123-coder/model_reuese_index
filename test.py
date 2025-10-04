import pandas as pd
from scripts.parse_assets import read_excel, search_excel, query_llm_with_excel

def main():
    # Path to the Excel file
    file_path = input("Enter the path to the Excel file: ")

    # Read the Excel file
    data = read_excel(file_path)
    if data is None:
        return

    # Display available columns
    print("\nAvailable columns in the Excel file:")
    print(data.columns.tolist())

    # Choose search method
    print("\nChoose a search method:")
    print("1. Traditional column-based search")
    print("2. LLM-based search")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        column_name = input("\nEnter the column name to search in: ")
        search_value = input("Enter the value to search for: ")

        results = search_excel(data, column_name, search_value)
        if results is not None and not results.empty:
            print("\nSearch Results:")
            print(results)
        else:
            print("\nNo matching results found.")
    elif choice == "2":
        query = input("\nEnter your query for the LLM: ")
        response = query_llm_with_excel(data, query)
        if response:
            print("\nLLM Response:")
            print(response)
        else:
            print("\nNo response from the LLM.")
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()