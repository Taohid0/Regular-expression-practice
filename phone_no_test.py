import re

phoneNumberRegex = re.compile(r"(013|017|019|018|016|015)(\d){8}")
searchObject = phoneNumberRegex.search("01710239959")
print(searchObject)