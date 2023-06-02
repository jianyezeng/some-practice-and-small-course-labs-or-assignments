alin_0={"color":'green','speed':'slow'}
point_value= alin_0.get('point','No point value assigned.') #当指定的键有可能不存在时，应考虑使用方法get()
print(point_value)

#练习6-1
person={'first_name':"Wang",
    'last_name':'Yizhu',
    'age':'21',
    'city':'Si Chuan'
    }
print(person)

#练习6-2
favorite_numbers={'lihua':'5','july':'9','lisa':'2','ganyu':'7','zhongli':'6'}
print(favorite_numbers)

#练习6-3答案
glossary = {
 'string': 'A series of characters.',
 'comment': 'A note in a program that the Python interpreter ignores.',
 'list': 'A collection of items in a particular order.',
 'loop': 'Work through a collection of items, one at a time.',
 'dictionary': "A collection of key-value pairs.",
 }
word = 'string'
print(f"\n{word.title()}: {glossary[word]}")
word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")
word = 'list'
print(f"\n{word.title()}: {glossary[word]}")
word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")
word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")

