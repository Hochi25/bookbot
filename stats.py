def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        i = 0
        for word in words:
            i += 1
    return i

def get_num_characters(file_path):
    with open(file_path) as c:
        text = c.read()
        characters = text.lower()
        dic = {}
        for char in characters:
         
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        return dic
    
def sort_on(items):
    return items["num"]

def get_form(dictionairy):
    form = []
    for k in dictionairy:
        form.append({"name": k, "num": dictionairy[k]})
    return form

def character_list(char_list):
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    