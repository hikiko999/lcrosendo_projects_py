import re

txt = "This a sample sentence"
x = re.search("Th.s", txt)
# First Match
print(x)

txt = "is a sample sentence"
x = re.findall(".+is", txt)
# One or more (No character at start of string)
print(x)

txt = "This is a sample sentence"
x = re.findall("\S*is", txt)
y = re.findall("\w*is", txt)
# Zero or more occurences -> No whitespace
# as long as no whitespace
print(x)
print(y)

txt = "This is a diss track"
x = re.search("\w*is\w*", txt)
print(x.group())