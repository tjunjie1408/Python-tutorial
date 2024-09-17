age = 25   #整数
height = 2.23 #浮点数
name = 'Ali'  #字符串，字符串""和''都可以
print(f"{name} is {age} years old and is {height} inches tall.")
print(  #普通算数运算符
2+5,
4-2,
10*12,
3/1)
print(  #特殊算数，//是取整数，%是取余数，**是指数意思就是平方和开方
    100//33,
    100%33,
    2**3,
    9**0.5
)
print(    #逻辑运算符，==是完全等于
    8>5,
    8<5,
    8>=5,
    8<=5,
    8==5
)
print(    #运算符
    True and True,
    True or True,
    not True
)
score = 70 #条件语句，if是如果，elif是其他如果，else是所有条件不符合
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D") #答案是C

for i in range(5): # for 循环，这段意思是让i循环5次，在计算机世界里0是第一个，所以答案是01234
    print(i)  

count = 0  # while 循环，只有结果为真实才会一直运行
while count < 5:
    print(count)
    count += 1 #如果没有这行那将会陷入死循环，答案是012345，+=的意思是自己加值
    
fruits = ["apple", "banana", "cherry", "date", 1, 1.2]  ##列表和元组，fruits是给列表赋值，注意fruits和fruit
#意思是给值取名字
for fruit in fruits: #这里使用for 循环一个个把列表里的值取出来
    print(fruit)
print(fruits[0]) #这里是从列表里第0个值给切出来，也就是apple因为0=1
print(fruits[1]) #0=1，所以1=2.答案是banana
print(fruits[-1])# 同理，-1就是列表最后一个值，答案是1.2
fruits.append("orange") #append是一个命令词，意思就是在末尾追加值
print(fruits) #答案就是['apple', 'banana', 'cherry', 'date', 1, 1.2, 'orange']

squares = [x**2 for x in range(5)]#这里使用for 循环和range快速创建列表，x^2的5次答案是[0, 1, 4, 9, 16]
squares = list(x**2 for x in range(5)) #list和 [] 方括号是等价，是一样的
print(squares)  #意思就是x从range(5)依次取出来然后进行2的平次方(x^2)的运算，最后把运算后的x存在一个列表(list)输出到终端(terminal)
#列表和元组是一个概念，基本一样但区别就是列表可以改变顺序，元组不能改变顺序
my_tuple = ("apple", "banana", "cherry", "date", 1, 1.2)
print(my_tuple)   #但是和list一样可以做切片动作比如， print(my_tuple[1])，这样答案就是banana
#list就是列表，tuple就是元组

#字典和集合，叫字典因为你需要找到对应的value和key来一个个输入进去
person = {"name": "Bob", "age": "30", "city": "NewYork"}
print(person["name"]) #你只能输入key不能输入value，这里的概念就是命令计算机找"name"这个key所代表的value，也就是"Bob"

person["job"] = "Engineer" #这里的话是新增key进字典里，只需要新建value就行了
print(person)

unique_numbers = {1, 222, 222, 33, 22233, 222} #集合也是花括号，但是他和字典的区别就是集合里的值是无序的，是唯一的，就算重复也不会重复输出
print(unique_numbers) #答案是{1, 22233, 222, 33}  答案无序，唯一，集合是set

#函数
def greet(name, greeting="Hello"): #定义函数需要使用def接着放函数的名字，跟着喜好放名字，然后设置函数的参数和返回值
    return f"{greeting}{name}" #我这里是因为上面写过了所以有默认值
print(greet("Bob"))  #如果没有默认值就需要写两次

def greet(name, greeting):
    return f"{greeting}{name}" 
print(greet("Bob", "Hello"))  #就像这样，就算有默认值你这里也可以写其他值给替换掉
#如果有默认值就不需要填参数

#模块和包
import math  #需要调用各种模块前必须引用或者调用(import)，不然会报错
print(math.pi) #答案是3.1415926等等，因为我调用math这个模块来计算圆周率，pi就是圆周率
#你也可以自创模块，只需要创建新的file，比如file名字叫tjj，我在里面写一个常量
#exp: def party(x):
#        return x**3
#然后我在import tjj，print(tjj.party(3)),那么输出的数就是27
#如果要调用外部库的话，假如是普通python版本就需要在terminal打： pip install numpy，这样的话就可以在pip商城下载了
#如果是conda版本的话，命令是： conda install numpy pandas matplotlib scikit-learn
