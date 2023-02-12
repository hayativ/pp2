import re

pattern3 = "[a-z]+_[a-z]+"

pattern4 = "[A-Z][a-z]+"

text = "The quick brown fox123 jumps over the lazy dog.b"
pattern5 = "a.*b$"

ans = re.findall(pattern5, text)
print(ans)