import sys

for line in sys.stdin:
    article_id, section_text = line.strip().split(",", 1)
    words = section_text.split()
    for word in words:
        print(word.lower() + "\t" + article_id)

