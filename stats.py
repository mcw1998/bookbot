def get_text_length(text):
    split_text = text.split()
    return len(split_text)

def get_characters(text):
    char_dict = {}
    for char in text:
        c = char.lower()
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    items = [{"char": ch, "num": n} for ch, n in char_counts.items() if ch.isalnum()]

    items.sort(key =  lambda item : item["num"], reverse = True)

    for item in items:
        print(f"{item["char"]}: {item["num"]}")

    return items
