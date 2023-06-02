#练习7-8
sandwich_orders=['saed','frfwq','wqdq']
finished_sandwiches = []
while sandwich_orders:
	sandwich=sandwich_orders.pop()
	print(f"I made your {sandwich} sandwich.")
	finished_sandwiches.append(sandwich)
for a in finished_sandwiches:
	print(a)

#练习7-9
sandwich_orders=['saed','pastraim','frfwq','wqdq','pastraim','pastraim']
finished_sandwiches=[]
print("Out of pastraim.")

while 'pastraim' in sandwich_orders:
	sandwich_orders.remove("pastraim")

while sandwich_orders:
	sandwich=sandwich_orders.pop()
	finished_sandwiches.append(sandwich)

for a in finished_sandwiches:
	print(a)

#练习7-10
places=[]

active = True

while active :
	place=input("\nIf you could visit one place in the world, where would you go? ")
	places.append(place)

	repeat=input("\nDo you want another person answer this question? (yes or no) ")
	if repeat == 'no':
		active = False
for place in places:
	print('\n'+place)