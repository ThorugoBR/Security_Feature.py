# Security_Feature
## This is a Python program that uses PAWNED API to Check your password in a safe way , running the check process of you password in your machine , keeping your password safe and sound
How this program works? 

Well, you type your password with a little help from hashlib library (https://docs.python.org/3/library/hashlib.html) your typed password is encoded into UTF-8 and then into SHA1 hash, this hash is splitted into 2 parts.
The 5 first characters are used into the PWNED API (https://haveibeenpwned.com/API/v3#PwnedPasswords) to request the remaining 35 characters from their database and a count value related to the full hash


Now the program has the 35 final characters to double check with the rest of your password, if found, the count number that comes with the data is displayed to the user.

# Simple String Example
    Hey there what is the password that you want to check ?
    Type here your password: 1234
    User typed  1234
    Fully hashed password  7110EDA4D09E062AA5E4A390B0A572AC0D2C0220
    Addrs https://api.pwnedpasswords.com/range/7110E
    Last 35 characters match DA4D09E062AA5E4A390B0A572AC0D2C0220 and the count 1371079
    The 1234 was found 1371079 times, you should change your password
# Special character Example 

    Hey there what is the password that you want to check ?
    Type here your password: "^Horse!^"
    User typed  ^Horse!^
    Fully hashed password  FA79AA93D7DE3227504F248D9600B0E672109A39
    Addrs https://api.pwnedpasswords.com/range/FA79A
    ^Horse!^ not found, amazing, you're safe to go baby !! 