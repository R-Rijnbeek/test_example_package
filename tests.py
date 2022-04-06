import os,io, re

def getconfigGIT():
    with open(os.path.join(".git","config"), "r", encoding="utf-8") as fh:
        return  fh.read()

a= getconfigGIT()

b=re.search(r'(?<=\[remote "origin"\]\n\turl = )((.|\n)*)(?=\.git)', a).group(1)

print(b)
    
