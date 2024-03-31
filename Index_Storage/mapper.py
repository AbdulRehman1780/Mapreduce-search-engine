import sys

for line in sys.stdin:
    word, doc_id, vector = line.strip().split("\t", 2)
    print(word + "\t" + doc_id + "\t" + vector)

