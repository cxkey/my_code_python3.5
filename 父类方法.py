class Base():
    def process(self):
        print('it is from base')

class Son(Base):
    def process(self):
        Base.process(self)
Son().process()
