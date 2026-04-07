import string
import os
import random

def universal_streamer(folder_path):
    """Shuffles and streams tokens from all .txt and .csv files in the folder."""
    translator = str.maketrans('', '', string.punctuation)
    
    # 1. Get and Shuffle files to prevent 'Format Bias'
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith(('.csv', '.txt'))]
        random.shuffle(files) 
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
        return

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # 2. Handle CSV Files
        if file_name.endswith('.csv'):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    next(f) # Skip header
                except StopIteration:
                    continue
                for line in f:
                    parts = line.strip().split(',')
                    for part in parts:
                        val = part.lower().strip()
                        if val: yield val
                        
        # 3. Handle TXT Files
        elif file_name.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    # Remove punctuation and split into words
                    words = line.lower().translate(translator).split()
                    for word in words:
                        yield word
