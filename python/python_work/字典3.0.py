user_0={
	'username':'efermi',
	'first':'enrico',
	'last':'fermi'
}
#遍历所有键值对
for key,value in user_0.items():
	print(f"\nKey:{key}")
	print(f"Value:{value}")

#遍历字典中所有键，可使用方法keys()
for cj in user_0.keys():
	print(cj)

for cj in user_0:                      #遍历字典时，会默认遍历所有的键，因此keys()可省略
	print(cj)

friends=['li','jone']
favorite_language={
	'jen':'python',
	'ben':'c',
	'li':'basic',
	'jone':'c++'
	}
for name in favorite_language.keys():
	print(f"Hi,{name.title()}!")
	if name in friends:
		print(f"\t{name.title()},I see you love {favorite_language[name]}!")

if 'erin' not in favorite_language.keys():
	print("erin,please take our poll!")

#按特定顺序遍历字典中的所有键
for name in sorted(favorite_language.keys()):
	print(f"{name.title()},thank you for taking the poll！")

#遍历字典中所有的值
for language in favorite_language.values():
	print(language.title())
#可使用集合set，集合中的每一个元素都是独一无二的
for language in set(favorite_language.values()):
	print(language.title())

#练习6-5
rivers={'nile':'egypt','changjiang':'China','abiua':'dwq dwdI'}
for name,value in rivers.items():
	print(f"The {name.title()} runs through {value.title()}")
for name in rivers.keys():
	print(name)
for value in rivers.values():
	print(value)

#练习6-6
names=['july','jone','sam','tom','jerry','mark','ben']
favorite_language={"july":'C','jone':'c++','ben':'python'}
for name in names:
	if name in favorite_language.keys():
		print(f"{name},thank you for taking the poll!")
	else:
		print(f"{name},please take our poll！")