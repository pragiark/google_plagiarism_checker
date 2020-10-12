from googlesearch import search
import random

#open and separate sentence and remove new lines
with open("C:/Users/Arkadiusz/Desktop/FV/Październik/check.txt", encoding="utf-") as file:
    text = (file.read())
    text = text.rstrip(".")
    text = text.replace("\n", "")
    sentences_list = text.split(". ")
    # print(sentences_list)
    # for listtext in sentences_list:
    #     listtext.lstrip("")
    #     print(f'"{listtext}"')

# select random sentences to check
list_len= len(sentences_list)
randoms = random.sample(sentences_list, 3)
# print(randoms)

# scrape plagiarism suspect from Google
for check in randoms:
    query = f'"{check}"'
    for j in search(query, tld='pl', lang='pl', num=10, start=0, stop=None, pause=7.0):
        print(j)

