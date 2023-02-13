import re
# 1) Write a regular expression that matches any string that contains the word "hello".
pattern1 = ".hello."
# 2) Write a regular expression that matches any string that starts with the word "hello".
pattern2 = "^hello."
# 3) Write a regular expression that matches any string that ends with the word "world".
pattern3 = ".world$"
# 4) Write a regular expression that matches any string that contains a digit (0-9).
pattern4 = '.\d.'
# 5) Write a regular expression that matches any string that contains only letters (no numbers or special characters).
pattern5 = "^[a-zA-Z]+$"
# 6) Write a regular expression that matches any string that contains only uppercase letters.
pattern6 = "^[A-Z]+$"
# 7) Write a regular expression that matches any string that contains only lowercase letters.
pattern7 = "^[a-z]+$"
# 8) Write a regular expression that matches any string that contains a combination of letters and numbers, but no special characters.
pattern8 = '^\w+$' #or "^[a-zA-Z0-9]+$"
# 9) Write a regular expression that matches any string that contains a word that starts with the letter "a" and ends with the letter "z".
pattern9 = "^a.*.z$"
# 10) Write a regular expression that matches any string that contains a URL 
pattern10 = "http://www.[a-z]+.com"
pattern10 = ".http://www.example.com."
text = "Hello world apple world"
match = re.search(pattern6, text)
 
if match:
    print("Yes")
else:
    print("Not found")