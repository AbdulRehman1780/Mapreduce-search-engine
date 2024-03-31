import sys

top_n = int(sys.argv[1])  

scores = []

for line in sys.stdin:
    doc_id, score = line.strip().split("\t")
    scores.append((doc_id, float(score)))

scores.sort(key=lambda x: x[1], reverse=True)

for i in range(min(top_n, len(scores))):
    print(scores[i][0] + "\t" + str(scores[i][1]))

