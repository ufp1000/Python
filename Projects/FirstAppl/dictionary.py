import json

data=json.load(open("data.json"))
j=1

def dict(k):
    return data[k]

word=input("Enter the Word: ")
output=dict(word)
if type(output)==list:
    for i in output:
        print(str(j)+" "+ i)
        j=j+1
else:
    print(output)
