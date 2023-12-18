# 4. Networking
# In this task you have the opportunity to solve problems closer to the real file. This implies that you have to combine your probability skills with the natural language processing field, aka NLP. The dataset you are going to use is a list of tweets, found here tweets.json
# Your task is divided into two topics.
# In the first one you have to deal with word frequency and finding out the most popular and interesting words.
# The second topic is about typing prediction. A good use case for typing prediction is a smart phone. While writing messages to your beloved friends is a cumbersome work to do (many taps on your display), the phone operating system usually comes with a typing prediction software. Now while you type your text a list of suggestions pops up at every keystroke. Your task would be to write programs that do something similar, naturally in a simplified version (no need to write mobile applications).
# The NLP part
# One of the main issues of text processing is breaking a text into words. At the first glance it seems to be an easy job. For instance, you have the sentence Today is a sunny day. Easy enough you just use the python built in function sentence.split() (where sentence is the string). Now you have a list of words. But as you know words in a text come hand in hand with characters like . , ! ? " and a bunch of others. So extracting words from a sentence like Now! Tell me what is your "problem"? is suddenly more difficult.
# NLP libraries hold extensive tools for text processing. In this lab you'll be only scratching the surface of NLP. The word extraction problem mentioned above can be solved with a simple function call. For python you can use the import nltk, but before that don't forget to pip install nltk.
# The dataset
# The data that you have in this laboratory work is a JSON string. It is a popular data format. One of the advantages is that it is easy to read. Also it's very easy to transpose the data into python primitives like lists, dictionaries, strings and integers. For that in your script you import json and now can use it like this result = json.loads(input_string_you_read_from_file). In the result is stored either a python list or a dictionary. That's easy.
# Frequency
# 4.1 Popular
# Write a program that prints the first 10 most frequently used words, and the number of times it was mentioned.
# Ex:
# the 352
# a 235
# at 120
# . . .
# 4.2 Nouns
# Write a program that prints the first 10 most frequently used nouns, and the number of times it was mentioned.
# 4.3 Proper nouns
# Write a program that prints the first 10 most frequently used proper nouns, and the number of times it was mentioned.
# 4.4 Frequency
# Write a program that receives a word as an input and draws a frequency bar chart. Every bar should represent the period of 1 month.
# 4.5 Popularity
# In our dataset we also have the number of likes and retweets for every message. This can give us some insight about the tweet's popularity. Hence we can compute some sort of rating. The popularity of nouns is computed by the following formula frequency * (1.4 + normRetweet) * (1.2 + normLikes). The values normRetweet and normLikes are the normalized values of retweets and likes for every word. To compute the number of likes and retweets for every word you just cumulatively collect the numbers from every tweet that the word was mentioned.
# Ex: There are 2 tweets that mention the noun program. The first tweet has 32 retweets and 87 likes. The second tweet has 42 retweets and 103 likes. The number of retweets of the word program is 32 + 42 and the number of likes is 87 + 103.
# Write a program that prints the first 10 most popular nouns. The popularity is defined by the computed rating discussed above.
# Typing prediction
# 4.6 Suggestion
# Write a program that receives as input an uncompleted word and prints 3 word suggestions, followed by their frequency. The suggestions should be based on the initial dataset and sorted by the word frequency, computed in the first problem.
# The input can be any uncompleted word.
# Ex. Input: app, Output: application (324), apple (164), appreciate (53). Where application has the highest frequency, apple the second highest etc.
# Ex. Input: pro, Output: programming (196), product (176), program (103). Again programming has the highest frequency.
# 4.7 Suggestion occurrences
# Write a program that receives as input a word and prints 3 word suggestions, followed by the suggestion occurrences.
# The suggestions should be selected in the following way. You have to go through your tweets dataset and identify every occurrence of the input word. At every occurrence collect the word that follows the input word. That is the suggestion you are looking for. And also don't forget to count the number of times you get the same suggestions. Ex: input like and you find 5 occurrences of beer and 2 occurrences of love labs. Your suggestion words would be beer and labs. But beer has a priority because it occurred more times in your dataset. Your task is to select the most relevant suggestions as in the one that occurred the most.
# The input can be any completed word.
# Ex. Input: love, Output: programming (5), cars (2), beer (2)
# Ex. Input: awesome, Output: party (10), language (4), framework (2)

import json
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter
import matplotlib.pyplot as plt

def min_max_scaling(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

tweets = read_json("tweets.json")
for i in range(len(tweets)):
    tweets[i]['words'] = word_tokenize(tweets[i]['text'])

all_words = [word for tweet in tweets for word in tweet['words']]



print("Problem 4.1\n10 most frequently used words")
word_counts = Counter(all_words)
i = 0
for word, count in word_counts.most_common():
    if word.isalnum(): # letters and numbers, excluding words with special characters
        print(f'{i+1}. {word}: {count}')
        i += 1
    if i == 10:
        break


print("\n\nProblem 4.2\n10 most frequently used nouns")
pos_tags = pos_tag(all_words)
# 'NN' represents a singular noun, and 'NNS' represents a plural noun
nouns = [word for word, tag in pos_tags if tag in ['NN','NNS'] and word != 'https' and word.isalnum()]
nouns_counts = Counter(nouns)
i = 0
for word, count in nouns_counts.most_common():
    print(f'{i+1}. {word}: {count}')
    i += 1
    if i == 10:
        break



print("\n\nProblem 4.3\n10 most frequently used proper nouns")
proper_nouns = [word for word, tag in pos_tags if tag in ['NNP', 'NNPS'] and word.isalpha() and word.isalnum()]
proper_nouns_counts = Counter(proper_nouns)
i = 0
for word, count in proper_nouns_counts.most_common():
    print(f'{i+1}. {word}: {count}')
    i += 1
    if i == 10:
        break



print("\n\nProblem 4.5\n10 most popular nouns based on the number of likes and retweets")
popularity = []
for word in nouns_counts.keys():
    sum_likes = 0
    sum_retweets = 0
    for tweet in tweets:
        if word in tweet['words']:
            sum_likes += tweet['likes']
            sum_retweets += tweet['retweets']
    popularity.append({"word": word,"likes": sum_likes,"retweets": sum_retweets,"frequency": nouns_counts[word]})
max_likes = max(popularity, key=lambda x: x['likes'])
max_retweets = max(popularity, key=lambda x: x['retweets'])
min_likes = min(popularity, key=lambda x: x['likes'])
min_retweets = min(popularity, key=lambda x: x['retweets'])

for i in range(len(popularity)):
    popularity[i]['normLikes'] = min_max_scaling(popularity[i]['likes'],min_likes['likes'],max_likes['likes'])
    popularity[i]['normRetweets'] = min_max_scaling(popularity[i]['retweets'], min_retweets['retweets'], max_retweets['retweets'])
    popularity[i]['score'] = popularity[i]['frequency']*(1.4+popularity[i]['normRetweets'])*(1.2*popularity[i]['normLikes'])

sorted_popularity = sorted(popularity,key=lambda x: x['score'], reverse=True)
for i in range(10):
    print(f"{i+1}. {sorted_popularity[i]['word']}: {sorted_popularity[i]['score']}")



print('\n\nProblem 4.6\ninput an uncompleted word and print 3 word suggestions, based on their frequency')
incomplete_word = input("Type the incomplete word: ")
suggestion = {}
for word in word_counts.keys():
    if word.startswith(incomplete_word):
        suggestion[word] = word_counts[word]
sorted_suggestion = sorted(suggestion.items(), key=lambda x: x[1], reverse=True)

i=0
for word,count in sorted_suggestion:
    print(f'{word}({count})',end=' ')
    i+=1
    if i==3:
        break



print("\n\nProblem 4.7\ninput a word and print 3 word suggestions, based on the suggestion occurrences")
complete_word=input("Write a complete word: ")
suggestion_word=[]
for i in range(len(all_words)-1):
    if complete_word==all_words[i] and all_words[i+1].isalnum():
        suggestion_word.append(all_words[i+1])
best_suggestion_word=Counter(suggestion_word).most_common()
for i in range(3):
    print(f'{best_suggestion_word[i][0]}({best_suggestion_word[i][1]})',end=' ')




print("\n\nProblem 4.4\nfrequency bar chart for given word over 1 month")
month = {i+1:0 for i in range(12)}
word = str(input("Input word: "))

for tweet in tweets:
    if word in tweet['words']:
        month[int(tweet['created_at'][5:7])]+=tweet['words'].count(word)

keys = list(month.keys())
values = list(month.values())

plt.bar(keys, values)
plt.xlabel('Months')
plt.ylabel('Frequency')
plt.title(f"Frequency of word '{word}'")
plt.show()
print(sum(month.values()))
