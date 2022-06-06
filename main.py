# Word counter program.

def read_file_content(filename):
    with open(filename, "r") as d:
        txt = d.read()
    
    return txt


def count_words(filename):
    text = read_file_content(filename)
    words = text.replace(".", "").replace("?", "").replace(",", "").split()  # exempting signs from the count.
    WordsCount = {}
    for i in words:
        WordsCount[i] = words.count(i)
    return print(WordsCount)


count_words("./story.txt")
