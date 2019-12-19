class T(object):
    def __init__(self):
        print("初始化完成")
    def haha(self):
        print("执行哈哈")

#重定义加法
class Vector():
    def __init__(self, argu1, argu2):
        self.argu1 = argu1
        self.argu2 = argu2
    def __repr__(self):
        print("实例化的时候执行了__repr__()")
        return "Vector({}, {})".format(self.argu1, self.argu2)
    def __add__(self, other):
        print('实例化的时候执行了__add__')
        x, y = [self.argu1+other.argu1, self.argu2+other.argu2]
        return Vector(x,y)

vec1 = Vector(3,4)
vec2 = Vector(9,2)
#print(vec1)
#print(vec1+vec2)

