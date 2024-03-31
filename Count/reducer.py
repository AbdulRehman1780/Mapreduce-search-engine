import sys

current_word = None
doc_count = 0

for line in sys.stdin:
    word, article_id = line.strip().split("\t")
    if current_word == word:
        doc_count += 1
    else:
        if current_word:
            print(current_word + "\t" + str(doc_count))
        current_word = word
        doc_count = 1

if current_word:
    print(current_word + "\t" + str(doc_count))

