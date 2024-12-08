import requests
import hashlib
import sys
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(firsts,tail):
    hashes=(line.split(':') for line in firsts.text.splitlines())
    for h,count in hashes:
        if h==tail:
            return count
    return 0
def _pwned_api_check(password):
    #check password if it exists in api response
    sha1password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first,tail=sha1password[:5],sha1password[5:]
    response=request_api_data(first)
    return get_password_leaks_count(response,tail)

def main(args):
    for password in args:
        count=_pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. Bad password')
        else:
            print(f'{password} fas not found. Perfect')
    return 'DONE'

if __name__=='__main__':
    main(sys.argv[1:])
