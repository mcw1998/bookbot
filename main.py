def main():

    frank_bookpath = "./books/frankenstein.txt"
    text = retrieve_text(frank_bookpath)
    words = count_words(text)
    char_analysis = count_letters(text)
    sorted_list = sort_list(char_analysis)

    print(f"~~~~~~~Book anslysis for {frank_bookpath}~~~~~~~~")
    for item in sorted_list:
        if not item['Char'].isalpha():
            continue
        else:
            print(f"{item['Char']} has {item['Num']} appearances")

def count_words(text):
    words = text.split()
    return len(words)

def retrieve_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    char_dict = {}

    for char in text:
        current_char = char.lower()
        char_dict[current_char] = char_dict.get(current_char, 0) + 1
    return char_dict

def sort_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({'Char': char, 'Num': dict[char]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list

def sort_on(d):
    return d["Num"]

main()