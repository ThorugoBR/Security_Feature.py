import requests
import hashlib
import sys
# API DOC in https://haveibeenpwned.com/API/v3#PwnedPasswords
# To use this, you have to open your command prompt and run this archive
# You can check just one or more passwords ,for multiple passwords you have to add a space between them
# if your password has special characters in the extremities put your password between quotation marks
# e.g "^yourpassword#!@"
# Write Pass_ch.py yourpassword1 yourpassword1 "^yourpassword#!@"


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching : {res.status_code}, check the api and try again')
    return res
def get_pass_leak_count(hashes,hash_to_check):
    hashes= (line.split(':')for line in hashes.text.splitlines())
    for api_hash, count in hashes:
        if api_hash == hash_to_check:
            return  count
    return 0
def pwned_api_check(password):
    #hash the password and check
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail=sha1password[:5],sha1password[5:]
    response = request_api_data(first5_char)
    return get_pass_leak_count(response,tail)
def main(args):

    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'The {password} was found {count} times, you should change your password')
        else:
            print(f' {password} not found, amazing, you\'re safe to go baby !! ')
    return 'Done !'

if __name__ =='__main__':
    sys.exit(main(sys.argv[1:]))

