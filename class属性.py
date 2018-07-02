class A:
  def m(self):
    print('A')

class B(A):
  def m(self):
    print('B')
    super().m()

class C(B):
  def m(self):
    print('C')
    # see the difference!
    print(1,__class__)
    print(2,__class__.__mro__)
    print(3,self.__class__.__mro__)
    print(4,self.__class__)
    __class__.__mro__[2].m(self)

class D(C):
  def m(self):
    print('D')
    super().m()

o = D()
o.m()