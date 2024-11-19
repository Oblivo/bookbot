def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    
    compile_report(text)
    

def count_words(text_file):
    return len(text_file.split())

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_char_num(text):
    lower_text = text.lower()
    char_nums = {}
    list_char_nums = []
    for char in lower_text:
        if char in char_nums:
            char_nums[char] += 1
        else:
            char_nums[char] = 1 
    for char in char_nums:
        c = {}
        c["name"] = f"{char}"
        c["num"] = char_nums[char]
        list_char_nums.append(c)
    return char_nums, list_char_nums

def sort_on(dict):
    return dict["num"]

def sort_char_nums(dict):
    return dict.sort(reverse=True, key=sort_on)

def compile_report(text): 
    num_words = count_words(text)
    list_char_nums = get_char_num(text)[1]
    list_char_nums.sort(reverse=True, key=sort_on)
    
    print("---Begin Book report ---")
    print(f"{num_words} words found in the document")
    for entry in list_char_nums:
        if entry["name"].isalpha():
            print(f"The character {entry["name"]} was found {entry["num"]} times")
    print("--- End of report ---")
    
main()