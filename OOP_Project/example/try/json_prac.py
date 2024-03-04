import json

class D :
    def __init__(self):
        self.__ant = 10
        self.__cat = 20
        self.__dog = "hong"
    def louis() :
        return 1000
    def to_dict(self) :
        return {"ant": self.__ant, "cat": self.__cat}
d = D()
d_dict = d.to_dict()
print(type(d_dict))
j_string = json.dumps(d_dict, indent=4)
print(j_string)
print(type(j_string))

new = json.loads(j_string)
print(new)
print(type(new))

with open("example.json","w") as outfile:
    json.dump(d_dict, outfile, indent=4)


