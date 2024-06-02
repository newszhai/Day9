python_count=0
f=open("word.text","r")
# content = f.read()
# count=content.count("python")
# print(f"python在文件中出现：{count}次")
for line in f:
    words=line.split()
    for word in words:
        if word == "python":
            python_count+=1
print(f"python在文件中出现：{python_count}次")
f.close()