alin_0={'color': 'green', 'points': 5}      #字典中可包含任意数量的键值对
print(alin_0['color'])
print(alin_0['points'])                     #要获取与键相关联的值，可依次指定字典名和放在方括号内的键

alin_0={'color': 'green', 'points': 5}

new_point=alin_0['points']
print(f"You just earned {new_point} points!")

print(f"You just earned {alin_0['points']} points!")

#添加键值对
alin_0={'color': 'green', 'points': 5}
print(alin_0)

alin_0['x_position']=0
alin_0['y_position']=25
print(alin_0)

#空字典
alin_0={}
alin_0['color']='yellow'
alin_0['points']='5'
print(alin_0)

alin_0['color']='green'                     #修改字典中的值
print(alin_0)




alin_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"0riginal x_position: {alin_0['x_position']}")
if alin_0['speed'] == 'slow':
	x_increment = 1
elif alin_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alin_0['x_position'] = alin_0['x_position'] + x_increment
print(f"New x_position: {alin_0['x_position']}")

alin_0['speed']='fast'
if alin_0['speed'] == 'slow':
	x_increment = 1
elif alin_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alin_0['x_position'] = alin_0['x_position'] + x_increment
print(f"New x_position: {alin_0['x_position']}")

#删除键值对
alin_0={'color': 'green', 'points': 5}

del alin_0['color']
print(alin_0)


#由类似对象组成的字典
favorite_language={
	'jen':'python',
	'ben':'c',
	'li':'basic',
	'jone':'c++'
	}
print(f"li's favorite language is {favorite_language['li'].upper()}.")