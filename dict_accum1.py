d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0, 'abcd_words': [], 'punct_words': []}


def breakout_1(some_str):
    for char in some_str:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            d['vowels'] += 1

        elif not char.isalpha():
            d['nonalpha'] += 1

        else:
            d['consonants'] += 1
    start_lst = []
    punc_lst = []
    for word in some_str.split():
        if word[-1] in ['.', '?', '!']:
            d['abcd_words'].append(word)
        if word[0] in ['a', 'b', 'c', 'd']:
            d['punct_words'].append(word)

    return d


str1 = "Just a small-town girl Livin\' in a lonely world! She took the midnight train goin\' anywhere. Just a city boy Born and raised in South Detroit. He took the midnight train goin\' anywhere? A singer in a smoky room. The smell of wine and cheap perfume? For a smile they can share the night It goes on and on, and on, and on. Strangers waiting Up and down the boulevard. Their shadows searching in the night! Streetlights people Livin\' just to find emotion! Hidin\' somewhere in the night!"

print(breakout_1(str1))