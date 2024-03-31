import sys

current_word = None
current_doc = None
word_count = 0

for line in sys.stdin:
    word, doc, count = line.strip().split("\t")
    count = int(count)
    if current_word == word and current_doc == doc:
        word_count += count
    else:
        if current_word:
            print(current_word + "\t" + current_doc + "\t" + str(word_count))
        current_word = word
        current_doc = doc
        word_count = count

if current_word:
    print(current_word + "\t" + current_doc + "\t" + str(word_count))

