# lqm-file-extractor

Python tool to extract text content from .lqm and .jlqm (QuickMemo+) files.
→ [Original Project](https://github.com/pporadzisz/lqm-file-extractor) ←

## Features

- **Extraction:** Extracts files from .lqm to their respective folders.
- **.txt Files:** Creates .txt files from the written content of each extracted .jlqm file.
- **Organizes Output:** All extracted .txt files are saved in a single folder called **extracted_texts**.
- **Includes Metadata:** Adds creation date, category, and memo ID to the extracted text files.
- **Error Handling:** Continues processing even if some files fail to extract and lists the errors at the end.

## Installation

### Linux

1. Download the `extract.py` file:

```
wget https://raw.githubusercontent.com/pporadzisz/lqm-file-extractor/master/extract.py
```

2. Make sure you have Python 3 installed:

```
python3 --version
```

## How to Use

Run the script by passing the path of the folder containing the .lqm files:

```
python3 extract.py path_to_lqm_files
```

### Example

#### Input

```
python3 extract.py /home/user/Downloads/quickmemo_plus
```

#### Output

```
##### QuickMemo+_190212_021335(1).lqm

Creation Date: 2019-02-12 02:13:35
Category: My memos
Memo ID: 123

Text:
I LOVE LINUX

##### QuickMemo+_190212_021340(1).lqm

Creation Date: 2019-02-12 02:13:40
Category: My memos
Memo ID: 124

Text:
My second text
```

## Step-by-Step Guide

1. Use the Share option in QuickMemo+ on your Android device.
2. Select all the notes and click the Share button.
3. Choose the QuickMemo+ File (.lqm) option.
4. Save the .lqm files to Google Drive or local storage.
5. Download the .lqm files to a single folder on your computer.
6. Download the `extract.py` script.
7. Run the script in the terminal:

   ```bash
   python3 extract.py /path/to/your/lqm/files
   ```

8. Check the `extracted_texts` folder for the extracted .txt files.

## Contributing

Feel free to fork this project and submit pull requests with improvements. For significant changes, please open an issue first to discuss the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

## Portuguese Version

For the Portuguese version of this README, please refer to [README.md](/README.md).
