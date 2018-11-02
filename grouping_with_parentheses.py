import re

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("my number is 415-555-4242")
print(mo.group(1), mo.group(2), mo.group())
