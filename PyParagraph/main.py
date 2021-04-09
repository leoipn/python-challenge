import os
import re

list_of_lenght_of_each_word  = []
list_of_words_in_a_paragraph = []

file_path = os.path.join('raw_data', 'paragraph_1.txt')
file = open(file_path,"r")

for line in file:
    words = line.split(" ")
    letter_count = len(words)
    
    for letters in words:
        lenght_of_each_word = len(re.sub("[,.\"]","",letters))
        list_of_lenght_of_each_word.append(lenght_of_each_word)

    paragraphs = re.split("(?<=[.!?]) +", line)
    sentence_count = len(paragraphs)
    
    for words in paragraphs:
        amount_of_words_in_a_paragraph = len(words.split(" "))
        list_of_words_in_a_paragraph.append(amount_of_words_in_a_paragraph)
    
average_letter_count = sum(list_of_lenght_of_each_word)/letter_count
average_sentences = sum(list_of_words_in_a_paragraph)/sentence_count

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {letter_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average letter count: {average_letter_count}")
print(f"Average Sentence Length: {average_sentences}")
file.close
