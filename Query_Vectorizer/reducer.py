import sys

query_vector = {}

for line in sys.stdin:
    word, _ = line.strip().split("\t")
    query_vector[word] = 1

print(query_vector)

