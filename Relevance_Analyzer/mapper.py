import sys

for line in sys.stdin:
    doc_id, vector = line.strip().split("\t", 1)
    doc_vector = eval(vector)  
    relevance_score = 0
    for word, tf_idf in doc_vector.items():
        if word in query_vector:
            relevance_score += tf_idf * query_vector[word]
    print(doc_id + "\t" + str(relevance_score))

