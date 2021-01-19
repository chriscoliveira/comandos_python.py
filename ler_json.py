import json

with open('arquivo.json','r') as file:
    d1_json = file.read()
    print(d1_json)
    d1_json = json.loads(d1_json)
    print(d1_json)


for k, v in d1_json.items():
    print(k,v)
    for k1, v1 in v.items():
        print(f'\t{k1},{v1}')
