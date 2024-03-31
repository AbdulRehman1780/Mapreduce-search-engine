import sys

query = sys.argv[1].lower().split()

for word in query:
    print(word + "\t1")

