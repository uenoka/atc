# PAST_1_F.py
def to_lower(word):
    new_word = ''
    for i in range(len(word)):
        if i == 0 or i == len(word)-1:
            new_word += word[i].upper()
        else:
            new_word += word[i]
    return new_word


S = input()
flg = False
words = []
cnt = 0
word = ''
for c in S:
    if c.isupper():
        cnt += 1
    if cnt % 2 == 1:
        word += c.lower()
    else:
        word += c.lower()
        words.append(word)
        word = ''
words.sort()
for word in words:
    word = to_lower(word)
    print(word, end='')
