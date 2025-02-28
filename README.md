# FastFileSearch

FastFileSearch is a high-performance Python script that searches for a specific file on all available drives in the system. The search automatically stops as soon as the file is found.

## Features
- Parallel processing using up to 4 CPU cores.
- Automatic search termination upon finding the file.
- Robust error handling for permission and system errors.

## How to Use
```bash
python fast_file_search.py
```

## System Requirements
- Python 3.8 or higher
- Windows 10 or higher (other systems not tested)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yowhatup999/FastFileSearch.git
cd FastFileSearch
```

2. Set up a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# source .venv/bin/activate     # On Linux/Mac
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python fast_file_search.py
```

## License
This project is licensed under the MIT License.

