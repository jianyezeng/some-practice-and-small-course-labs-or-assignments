#字典列表
alin_0={'color':'red','points':15}
alin_1={'color':'yellow','points':10}
alin_2={'color':'green','points':5}
alins=[alin_0,alin_1,alin_2]
for alin in alins:
	print(alin)

alins=[]
for alin_number in range(0,30):
	new_alin ={'color':'green','points':5,'speed':'slow'}
	alins.append(new_alin)
for alin in alins[:5]:
	print(alin)
print("...")
print(f"Total number of alins:{len(alins)}")

for alin in alins[:3]:
	if alin['color']=='green':
		alin['color']='yellow'
		alin['points']=10
		alin['speed']='medium'
for alin in alins[:5]:
	print(alin)

#在字典中存储列表
top=['mushrooms',"extra cheese"]
pizza={'crust':'thick','toppings':top}
print(pizza)

print(f"You ordered a {pizza['crust']}-crust pizza with the following topppings:")
for topping in pizza['toppings']:
	print(topping)
favorite_language={'ben':['c++','basic'],'july':['c','c#'],'sam':['python','B'],'amy':['go','matalb']}
for name,languages in favorite_language.items():
	print(f"{name.title()}'s favorite languages are:")
	for language in languages:
		print(language)

#在字典中存储字典
users={'jum':{'first':1,'last':2},'dda':{"first":6,'last':5}}
print(users)
for username,usernum in users.items():
	print(f"user:{username}")
	print(f"\t{usernum['first']}")
	print(f"\t{usernum['last']}")
