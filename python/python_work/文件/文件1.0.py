# with open('pi_digits.txt') as file_object:            #相对路径或绝对路径
# 	contents = file_object.read()
# print(contents.rstrip())

# with open('txt/2.0.txt') as file_object:
# 	contents = file_object.read()
# print(contents)

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# pi_strings = ''
# for line in lines:
# 	pi_strings += line.strip()

# print(pi_strings)
# print(len(pi_strings))

#练习10-1
with open('learning_python.txt') as file_0:          #读取整个文件
	lines = file_0.read()
print(lines.strip())

with open('learning_python.txt') as file_0:          #遍历整个文件对象
	for line in file_0:
		print(line.rstrip())

with open('learning_python.txt') as file_0:          #先存在一个列表中
	lines = file_0.readlines()

message = ''
for line in lines:
	message += line.rstrip()
print(message)

#练习10-2
message = "I really like a dog."
message = message.replace('dog','cat')                 #replace()方法可暂时将字符串中的特定单词替换为另一个单词

print(message)

with open('learning_python.txt') as file_0:
	lines = file_0.readlines()

for line in lines:
	line = line.replace('python','C').rstrip()
	print(line)