"""
Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""

ONES = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
TEENS = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
TENS = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

def say(n: int) -> str:
    o = n % 10
    t = n % 100 - o
    h = n % 1000 - t - o
    
    string = ''
    
    if h:
        string += f'{ONES[h//100]}hundred'
        
        if t or o:
            string += 'and'
    
    if t:
        if t + o in TEENS:
            string += f'{TEENS[t + o]}'
            return string

        else:
            string += f'{TENS[t]}'
    
    if o:
        string += f'{ONES[o]}'

    return string

letters = len('onethousand')
for i in range(1, 1000):
    letters += len(say(i))

print(letters)
