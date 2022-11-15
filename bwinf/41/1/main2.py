import re

# sets the filename for the book and the task
bookfile = "Alice_im_Wunderland.txt"
taskfile = "stoerung0.txt"

# reading the book and the task
book = open(bookfile, encoding="utf-8").read().split()
task = open(taskfile, encoding="utf-8").read().split()


# methode to remove all special characters from a String list
def sub(sub_list):
    return [re.sub(r'[^a-zäöüß]', '', word.lower()) for word in sub_list]


# methode to get the index of the sublist from an list
def sublist_index(main_list, sub_list):
    for i in range(len(main_list)):
        if main_list[i] == sub_list[0]:
            n = 1
            while (n < len(sub_list)) and (main_list[i + n] == sub_list[n]):
                n += 1
            if n == len(sub_list):
                return i
    return None


# formatting of the books
book = sub(book)

# changing each word that is not in the task to an "_"
temp_book = [word if word in task else "_" for word in book]

# finding the task in the book and getting the index of it
index = sublist_index(temp_book, task)

# print the solution
print(" ".join(book[index:index + len(task)]))
