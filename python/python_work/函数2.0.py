#返回值
def get_formatted_name(first_name,last_name):
	"""返回整洁的姓名。"""
	full_name=f"{first_name} {last_name}"
	return full_name.title()

musician=get_formatted_name("jimi",'hendrix')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
	"""返回整洁的姓名。"""
	full_name=f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician=get_formatted_name("jimi",'hendrix')
print(musician)

#返回字典
def build_person(first_name,last_name,age=None):
	"""返回一个字典，其中包含一个人的信息"""
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person 
musician = build_person("jie",'hendrix','8')
print(musician)

#结合使用函数与while循环
# def get_formatted_name(first_name,last_name):
# 	"""返回整洁的姓名。"""
# 	full_name=f"{first_name} {last_name}"
# 	return full_name.title()
# while True:
# 	print("\nPlease tell me your name: ")
# 	f_name = input("First name: ")
# 	l_name = input("Last name: ")

# 	full_name=get_formatted_name(f_name,l_name)
# 	print(f"Hello {full_name}!")

# 	message=input("\nDo you want another person answer this question? (yes or no) ")
# 	if message == 'no':
# 		break

#练习8-6
def city_country(city,country):
	"""显示城市名及其国家"""
	print(f"{city.title()},{country.title()}")

city_country('santiago','chile')

#练习8-7
def make_album(name,zhuj):
	"""返回一个包含歌手名字和专辑名的字典"""
	songs={'singer':name,'song':zhuj}
	return songs

#练习8-8
def make_album(name,zhuj):
	"""返回一个包含歌手名字和专辑名的字典"""
	songs={'singer':name,'song':zhuj}
	return songs

while True:
	print("请输入歌手名字和专辑名：")
	name=input("歌手名字： ")
	zhuj=input('专辑名字： ')
	sda=make_album(name,zhuj)
	print(sda)
	print(f"{sda['singer'].title()} : {sda['song'].title()}")

	message=input("是否继续输入：(是 或 否)")
	if message == '否':
		break