# Security_Feature
## This is a Python program that uses PAWNED api to Check your password in a safe way , running the check process of you password in your machine , keeping your password safe and sound
How this program works? 

Well, you type your password with a little help from hashlib library (https://docs.python.org/3/library/hashlib.html) your typed password is encoded into UTF-8 and then into SHA1 hash, this hash is splitted into 2 parts.
The 5 first characters are used into the PWNED API (https://haveibeenpwned.com/API/v3#PwnedPasswords) to resquest the remaining 35 characters from their database and a count value related to the full hash


Now the program has the 35 final characters to double check with the rest of your password, if found, the count number that comes with the data is displayed to the user.


