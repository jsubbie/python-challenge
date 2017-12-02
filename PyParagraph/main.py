import os 
import csv 
import re 

with open ('first_verse.txt') as f: 
    text = f.read().replace("\n", " ")
    sentences = re.split("(?<=[.?!]) + ", text) 
    
   #word count  
    word_count = len(re.findall(r'\w+', text))
   
   # sentence count 
    sentence_count = len(sentences)

    # average letter count by word      
    letters = len(re.findall('[A-Za-z]', text))
    letter_avg = (letters/word_count)

    # average sentence length by word
    sent_avg = (word_count/sentence_count) 

print(text)
print("--------------------")    
print("Paragraph Analysis")
print("--------------------") 
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average letter count (per word) " + str(letter_avg))
print("Average sentence lenth (in words) " + str(sent_avg))

# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)