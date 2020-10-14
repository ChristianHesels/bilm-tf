
from collections import defaultdict
import sys

def read_tuebadz_per_sentence(path):
    i = 0
    raw_data = {}
    gold_standard = {}
    sentences = []
    _sent = ""
    for line in open(path,'r').readlines():
        li=line.strip()
        if not li.startswith("#") and not li.startswith("\n"):
            if li:
                li = li.split()
                _sent += li[3] + " "
            else:
                sentences.append(_sent)
                _sent = ""
            
        #if i == 1000:
        #    break
        #i += 1
    return sentences, gold_standard
if len(sys.argv) == 3:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    raw_sentences, gold_standard = read_tuebadz_per_sentence(input_path)
    with open(output_path, 'w') as f:
        for sentence in raw_sentences:
            f.write("%s\n" % sentence)
else:
    print("Usage:")
    print("python3 parse_tuebadz.py <input-file> <output-file>")

