class test():
    pass
print(test) #类也是一个对象，test表示类对象（不是类的实例），test()表示类的实例
print(test())

MyShinyClass = type('MyShinyClass', (), {})  # 返回一个类对象
print(MyShinyClass)

# 1、构建Foo类
#构建目标代码
class Foo(object):
    bar = True
#使用type构建
Foo = type('Foo', (), {'bar':True})

# 2.继承Foo类
#构建目标代码：
class FooChild(Foo):
    pass
#使用type构建
FooChild = type('FooChild', (Foo,),{})

print(FooChild)
#输出：<class '__main__.FooChild'>
print(FooChild.bar)   # bar属性是由Foo继承而来
#输出：True

# 3.为Foochild类增加方法
def echo_bar(self):
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
hasattr(Foo, 'echo_bar')
#输出：False
hasattr(FooChild, 'echo_bar')
#输出：True
my_foo = FooChild()
my_foo.echo_bar()
#输出：True