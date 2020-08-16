from nltk.tokenize import word_tokenize
# import nltk
# nltk.download()
# Natural Language Toolkit (NLTK)


def process_message(message, lower_case=True, gram=2):
    if lower_case:
        message = message.lower()
    words = word_tokenize(message)
    words = [w for w in words if len(w) > 2]
    print('Initial', words)
    if gram > 1:
        w = []
        for i in range(len(words) - gram + 1):
            w += [' '.join(words[i:i + gram])]
        return w
    return words


pm = process_message('congatulations you are awarded $500')
print('final', pm)

pm = process_message('I cant pick the phone right now. please send a message')
print('final', pm)


