import re
def f(snake_string):
     return snake_string.title().replace("_", "")
txt = input()
pattern = "(?P<g1>[a-z])_(?P<g2>[A-Z])+"
print(re.sub(pattern, f, txt))

# "(?P<g1>[a-z])(?P<g2>[A-Z])+"

#mObject.group("g1")+ "_" + mObject.group("g2").lower()