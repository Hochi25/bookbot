def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        i = 0
        for word in words:
            i += 1
    return f"Found {i} total words"