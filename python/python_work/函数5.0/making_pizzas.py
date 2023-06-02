# #导入整个模块
# import pizza

# pizza.make_pizza(16,'pepperroni')
# pizza.make_pizza(12,'mushroom','green peppers','extra cheese')

# # #导入特定的函数
# # from module_name import function_name
# # #可根据需要从模块中导入任意数量的函数
# # from module_name import function_1,function_2,function_3

# from pizza import make_pizza

# make_pizza(16,'wdqdq')

# #由于导入函数的名称可能与程序中现有的名称冲突，
# #或者函数的名称过长，可以指定一个别名

# #使用as给函数指定别名

# from pizza import make_pizza as mp

# mp(145,'wdqwd')


# #使用as给模块指定别名
# import pizza as p

# p.make_pizza(5,'adwd')

#导入模块中的所有函数
from pizza import *                 #使用星号可导入模块中所有函数，因此之后不用使用句点表示法
                                    #但可能覆盖原有函数，因此不建议使用
make_pizza(16,'eafaf')