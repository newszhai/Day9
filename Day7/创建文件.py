f = open('python.txt',"r")
# for i in range(100):
#     print(i,file=f)
'''content = f.readlines()
print(content)'''
# for i in range(100):
#  content = f.readline()
#  print(f'第{i}行：{content}')
#
# f.close()
'''for line in open('python.txt','r'):
    print(line,end='')'''
    
with open("python.txt","r")as f:
  content=f.readlines()
  print(content)
