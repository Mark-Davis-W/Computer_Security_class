#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse, urlunparse
from pymd5 import md5, padding


##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here
    #Parsing up the url
    query = url.query
    firstPos = query.find("token=")
    secondPos = query.find("&")
    oldCommands = query[secondPos+1:]
    newCommand = "&command=UnlockSafes"
    #length of old commands plus known 8 byte password length
    len_of_command = len(oldCommands) + 8
    #bits of of the block based off the previous
    bits = (len_of_command + len(padding(len_of_command*8)))*8
    #extract the token hex
    token = query[firstPos+6:secondPos]
    #Initialize hash at current state
    hStart = md5(state=bytes.fromhex(token), count=bits)
    hStart.update(newCommand)
    #replace the token with new token
    query = query.replace(query[firstPos+6:secondPos],hStart.hexdigest())
    #calculae padding and use quote to pass url safe
    paddit = quote(padding(len_of_command*8))
    #replace the whole backend after the token and first & with new data
    query = query.replace(q[secondPos+1:], oldCommands + paddit + newCommand)
    #replace the whole query in url with newly made query 
    url = url._replace(query = query)

    #finally print out unparsed url
    print(urlunparse(url))








