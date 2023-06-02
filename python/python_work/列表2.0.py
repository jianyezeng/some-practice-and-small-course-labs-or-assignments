team=["mike","jone","tom","sam"]
team.sort()                           #sort可对列表进行永久排序
print(team)                           #team.sort()
team.sort(reverse=True)
print(team)
print(team.sort(reverse=True))

team=["mike","jone","tom","sam"]
print(team)                           #sorted可对列表暂时排序
print(sorted(team))                   #sorted(team)
print(team)                           #sorted(team,reverse=True)
print(sorted(team,reverse=1))
print(team)

team=["mike","jone","tom","sam"]
team.reverse()                        #reverse可永久性改变列表顺序（反方向）
print(team)
team.reverse()
print(team)
###print(team.reverse())              #？？？


print(len(team))                      #函数len()可快速获悉列表的长度


#练习3-8
place=["Beijing","Shanghai","London","New York","Chengdu"]
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=1))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)