result=[]
with open("5ban.txt","r",encoding='utf-8')as fin:
    for line in fin:
        line = line[:-1]
       # print(line,type(line))#101,小花,65 <class 'str'>
        list_read=line.split(",")
        result.append((list_read))
       # print("result",result)#result [['101', '小花', '65'], ['102', '小李', '75'], ['103', '小红', '55'], ['104', '小子', '4']]
print(sorted(result,key=lambda x:int(x[2])))
# students = []
# with open('5ban.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         parts = line.strip().split(',')
#         student_id, name, score = parts[0], parts[1], int(parts[2])
#         students.append({'id': student_id, 'name': name, 'score': score})
# students_sorted = sorted(students, key=lambda x: x['score'], reverse=True)
# for student in students_sorted:
#     print(f"学号: {student['id']}, 姓名: {student['name']}, 成绩: {student['score']}")