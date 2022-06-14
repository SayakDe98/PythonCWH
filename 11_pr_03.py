class Sample:
    a="Harry"#class attribute

obj=Sample()
obj.a="Vikky"#Sets a new instance attribute
#Sample.a="Vikky"#this changes class attribute

print(Sample.a)
print(obj.a)