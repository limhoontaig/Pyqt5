import os
list_a = []
for (path, dir, files) in os.walk("e:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            l = list_a.append(filename)

print("%s/%s" % (path, filename))
print()
print(l)