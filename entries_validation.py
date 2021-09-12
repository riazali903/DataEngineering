
import json

with open('record.json') as f:
    vari =json.load(f)


vari.sort(key=lambda k: int(k['Name'].split("_")[1]))
# print(json.dumps(vari, indent=4, sort_keys=True))
print(f'Total size {len(vari)}')

i = 0
for n in vari:
    print(n["Name"], " - ", n["Searches"])
    i += n["Searches"]

print(f'Total searches {i}')

