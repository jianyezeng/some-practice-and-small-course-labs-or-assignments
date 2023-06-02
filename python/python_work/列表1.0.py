family=["a","b","c"]
print(family)
family[0]="s"
family.insert(0,family[0])
print(family)
del family[0]
print(family)
popped_family=family.pop(2)
print(family)
print(popped_family)
cppos="b"
family.remove("b")  #remove只删除第一个指定的值,如果要删除多个，需要使用循环
print(family)
print(cppos)
#练习3—4
ker=["Li ming","Li hua","Mike"]
print(f"{ker[0]} ,{ker[1]} ,{ker[2]} 请和我共进晚餐。")
#练习3—5
print("Mike无法赴约")
ker.remove("Mike")
ker.append("Jone")
print(f"{ker[0]} ,{ker[1]} ,{ker[2]} 请和我共进晚餐。")
#练习3—6
print("我找到了一个更大的餐桌")
ker.insert(0,"Wang wei")
ker.insert(2,"July")
ker.append("Michael")
print(f"{ker[0]},{ker[1]},{ker[2]},{ker[3]},{ker[4]},{ker[5]}请和我共进晚餐。")
#练习3-7
print("我只能邀请两个人共进晚餐")
popped_ker=ker.pop(2)
print(f"{popped_ker}我很抱歉，不能和你共进晚餐")
popped_ker=ker.pop(2)
print(f"{popped_ker}我很抱歉，不能和你共进晚餐")
popped_ker=ker.pop(2)
print(f"{popped_ker}我很抱歉，不能和你共进晚餐")
popped_ker=ker.pop(2)
print(f"{popped_ker}我很抱歉，不能和你共进晚餐")
print(ker[0]+"我们将共进晚餐。")
print(ker[1]+"我们将共进晚餐。")
#练习3-9
print(len(ker))

del ker[0]
del ker[0]
print(ker)
