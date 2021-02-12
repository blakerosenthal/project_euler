"""
Problem 22: Names scores

Using names.txt, a 46K text file containing over
five-thousand first names, begin by sorting it
into alphabetical order. Then working out the
alphabetical value for each name, multiply this
value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical
order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain
a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

with open('data/p022_names.txt') as f:
    names_raw = f.read()

names = sorted([name.strip().replace('"', '') for name in names_raw.split(',')])
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()

all_scores = 0
for name in names:
    position_score = names.index(name) + 1
    letters_score = 0
    for letter in name:
        letters_score += alphabet.index(letter) + 1
    
    all_scores += position_score * letters_score

print(all_scores)
