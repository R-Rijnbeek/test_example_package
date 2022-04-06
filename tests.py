import os,io, re

def getPacketInitFileContent():
    return io.open(
            os.path.join('src', "robert_rijnbeek_package",'__init__.py'),
            encoding='utf_8_sig'
            ).read()

a = getPacketInitFileContent()
print(a)

print(re.search(r'(?<=\"\"\")((.|\n)*)(?=\"\"\")', a).group(1))

