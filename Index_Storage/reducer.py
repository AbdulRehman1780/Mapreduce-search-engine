import sys

index = {}

for line in sys.stdin:
    word, doc_id, vector = line.strip().split("\t", 2)
    if word not in index:
        index[word] = {}
    index[word][doc_id] = vector

print(index)

