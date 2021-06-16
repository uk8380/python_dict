#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*,
#changeable and does not allow duplicates.
#syntax below
uk = {
  "brand": "tesla",
  "model": "tes-1",
  "year": 2020
}
print(uk)
#can acess values
print(uk["year"])
print(len(uk))
print(type(uk))
x=uk["model"]
print(x)
#alternate
y=uk.get("year")
print(y)
z=uk.keys()
print(z)
uk["color"]="red"
print(uk)
uk.get("color")
print(uk["color"])
print(uk.update({"year":2021}))
print(uk.pop("color"))
print(uk)#while using del function use["model"]..syntax:del uk["color]
#copying dict
uko=uk.copy()
print(uko)
#alternate
uka=dict(uko)
print(uka)
#nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
