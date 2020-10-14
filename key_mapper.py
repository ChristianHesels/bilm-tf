from collections import defaultdict
import h5py
import numpy as np
import sys

vector_dict = defaultdict(list)

if len(sys.argv) == 4:
    tuebadz_path = sys.argv[1]
    lm_file = h5py.File(sys.argv[2], "r")
    output_path = sys.argv[3]
    with open(tuebadz_path, 'r') as outfile:
        lines = outfile.readlines()
        i = 0
        same_sentence = False
        for line in lines:
            li=line.strip()
    
            if not li.startswith("#"): 
                if li:
                    if not same_sentence:
                        _ = line.split()
                        vector_dict[_[0]].append(lm_file[str(i)])
                        same_sentence = True
                else:
                    same_sentence = False
                    i += 1
                    
    
    
    hf = h5py.File(output_path, 'w')
    for key in vector_dict:
        try:
            _group = hf.create_group(key)
            [_group.create_dataset(key + "." + str(i), data=np.array(sentence)) for i, sentence in enumerate(vector_dict[key])]
        except Exception as e:
            print(e)
            hf.close()
            break
    hf.close()
else:
    print("Usage:")
    print("python3 key_mapper.py <tuebadz-file> <hdf5-input-file> <hdf5-output-file>")