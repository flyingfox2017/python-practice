#python 六种数据类型
    #Number(数字)
    #String(字符串)
    #List(列表)
    #Tuple(元组)
    #Set(集合)
    #Dictionary(字典)

# Number Python3 支持 int、float、bool、complex（复数）。
# a,b,c,d = 20,4.5,True,4+3j
# print(type(a),type(b),type(c),type(d))


#List 与字符串不一样的是, List列表中的元素是可变的.
listA = ['a','b','c','d','e']

#从第一个开始截取, 截到第一个为止.
print(listA[0:1])

#从第一个开始截取,截到第3个为止
print(listA[0:3])

#从第一个开始截取,截取到倒数第二个为止.
print(listA[0:-1])


#Tuple 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。元组中的元素类型也可以不相同：
tuple = ('abdc',123,2.23)

print(tuple)


#set()集合是一个无序不重复的序列 基本功能是进行成员关系测试和删除重复元素。可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack'}

print(student)  # 输出集合，重复的元素被自动去掉
if 'Rose' in student:
    print("Rose 在 student")
else:
    print("not in")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素


# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
#
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
#
# 键(key)必须使用不可变类型。
#
# 在同一个字典中，键(key)必须是唯一的。

tinydict = {"a":123,"b":True,"c":"string123"}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())