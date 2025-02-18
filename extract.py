import os
import zipfile
import json
import sys
from datetime import datetime

# Main function to extract content from .lqm files
def main():
    # Check if the path is provided as an argument
    if len(sys.argv) < 2:
        print("Please provide the path to the folder containing .lqm files.")
        print("Por favor, forneça o caminho da pasta contendo os arquivos .lqm.")
        sys.exit(1)

    path = sys.argv[1]  # Path to the folder containing .lqm files
    errors = []  # List to store errors encountered during extraction

    # Create the 'extracted_texts' folder if it doesn't exist
    output_folder = os.path.join(path, "extracted_texts")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Folder '{output_folder}' created to store .txt files.")
        print(f"Pasta '{output_folder}' criada para armazenar os arquivos .txt.")

    # Iterate over all files in the specified folder
    for file_name in os.listdir(path):
        if file_name.endswith(".lqm"):
            abs_file_path = os.path.join(path, file_name)  # Absolute path to the .lqm file

            # Create the output path for extraction
            parent_path = os.path.split(abs_file_path)[0]
            output_folder_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(parent_path, output_folder_name)

            try:
                # Extract the content of the .lqm file (which is a zip file)
                with zipfile.ZipFile(abs_file_path, 'r') as zip_obj:
                    zip_obj.extractall(output_path)

                # Path to the extracted memoinfo.jlqm file
                memoinfo_path = os.path.join(output_path, 'memoinfo.jlqm')

                # Read the content of the memoinfo.jlqm file
                with open(memoinfo_path, 'r', encoding='utf-8') as memoinfo_file:
                    memoinfo_data = json.load(memoinfo_file)

                # Try to get the text from the 'DescRaw' field
                try:
                    memo_text = memoinfo_data['MemoObjectList'][0]['DescRaw']
                except KeyError:
                    # If the 'DescRaw' field doesn't exist, add the file to the error list
                    errors.append(file_name)
                    print(f"Error: 'DescRaw' field not found in file {file_name}.")
                    print(f"Erro: Campo 'DescRaw' não encontrado no arquivo {file_name}.")
                    continue

                # Get the creation time of the memo (in milliseconds since Unix epoch)
                created_time_ms = memoinfo_data['Memo']['CreatedTime']
                # Convert to the American format (YYYY-MM-DD HH:MM:SS)
                created_time = datetime.fromtimestamp(created_time_ms / 1000).strftime('%Y-%m-%d %H:%M:%S')

                # Create a .txt file with the same name as the .lqm file
                txt_file_name = os.path.splitext(file_name)[0] + ".txt"
                txt_file_path = os.path.join(output_folder, txt_file_name)  # Save in the 'extracted_texts' folder

                # Write the metadata and extracted content to the .txt file
                with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                    # Add metadata
                    txt_file.write(f"Created Time (Data de Criação): {created_time}\n")
                    txt_file.write(f"Category (Categoria): {memoinfo_data['Category']['CategoryName']}\n")
                    txt_file.write(f"Memo ID (ID do Memo): {memoinfo_data['Memo']['Id']}\n")
                    txt_file.write("\n")  # Blank line to separate metadata from content
                    # Add the memo content
                    txt_file.write(memo_text)

                print(f"##### {file_name} #####")
                print("Text extracted successfully and saved to:", txt_file_path)
                print("Texto extraído com sucesso e salvo em:", txt_file_path)
                print("")

            except Exception as e:
                # Capture other errors that may occur during extraction
                errors.append(file_name)
                print(f"Error processing file {file_name}: {e}")
                print(f"Erro ao processar o arquivo {file_name}: {e}")
                continue

    # Display errors at the end of execution
    if errors:
        print("\nErrors encountered during extraction:")
        print("Erros encontrados durante a extração:")
        for error_file in errors:
            print(f"- {error_file}")
    else:
        print("\nAll files were extracted successfully!")
        print("Todos os arquivos foram extraídos com sucesso!")

if __name__ == "__main__":
    main()