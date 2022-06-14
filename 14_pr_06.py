from unicodedata import name


class Sample:
    a="Harry"
    def __init__(slf,name):
        slf.name=name#we can use any valid identifier instead of self too
obj=Sample("Harry")
obj.a="Vikky"
print(obj.name)