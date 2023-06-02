#练习6-7
persons=[]
person_0={'name':'july','city':'Beijing','age':16}
persons.append(person_0)
person_1={'name':'Amy','city':'Xian','age':18}
persons.append(person_1)
person_2={'name':'daming','city':'New York','age':17}
persons.append(person_2)
for person in persons:
	print(f"{person['name'].title()},of {person['city']},is {person['age']} years old.")

#练习6-8
pet_0={'style':'dog','host':'amy'}
pet_1={'style':'cat','host':'jone'}
pet_2={'style':'bird','host':'july'}
pets=[pet_0,pet_1,pet_2]
for pet in pets:
	print(f"This {pet['style']}'s host is {pet['host']}.")

#练习6-9
favorite_place={}
place_1=['beijing','xianggang']
place_2=['luoyang','xian']
place_3=['eqgy','london']
favorite_place['july']=place_1
favorite_place['ben']=place_2
favorite_place['amy']=place_3
for name,place in favorite_place.items():
	print(f"{name.title()}'s favorite places are :")
	for place in favorite_place[name]:
		print(f"\t{place}")

#练习6-10
favorite_numbers={}
favorite_numbers['Amy']=[1,2]
favorite_numbers['Ben']=[3,4]
favorite_numbers['July']=[5,6,7]
for name,numbers in favorite_numbers.items():
	print(f"{name.title()}'s favorite numbers are:")
	for number in favorite_numbers[name]:
		print(f"\t{number}")

#练习6-11
cities={}
cities['city_0']={'country':'China','number':'50000','feature':'freedom'}
cities['city_1']={'country':'England','number':'62040','feature':'wizedom'}
cities['city_2']={'country':'USA','number':'84524','feature':'modern'}
print(cities)
for city,fact in cities.items():
	print(f"{city} {fact['country']} {fact['number']} {fact['feature']}")