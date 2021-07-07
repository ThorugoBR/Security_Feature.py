# Security_Feature.py
## This is a Python program that uses PAWNED api to Check your password in the safest way possible , running the check process of you password in your machine , keeping your password safe and sound
How this program work? 
Well, you type your password with a little help from hashlib library (https://docs.python.org/3/library/hashlib.html) your typed password is encoded into sha1 hash this hash is splitted into 2 parts.
The 5 first characters are used into the PWNED API (https://haveibeenpwned.com/API/v3#PwnedPasswords); this 5 characters are used to request all data from their database that has the same 5 first characters, this data is sent to you and all hashed passwords are checked inside of your local machine if any full hash that came to you is equal to your hashed password that means your passord has been leaked and add one to the counter.

