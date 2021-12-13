#Python program to create to url shortner using an API

"""
First we have to import 7 libraries.
We could have used just one library to work,
but in order to make good url shortener we have to use 7 libraries.
"""

from __future__ import with_statement                                                        
  
import contextlib
  
try:
    from urllib.parse import urlencode          
  
except ImportError:
    from urllib import urlencode
  
try:
    from urllib.request import urlopen
  
except ImportError:
    from urllib2 import urlopen
  
import sys

#  encoding of url and appending it to API is done 
# and then we open request_url using urlopen. 
# Then we convert the response to UTF-8, 
# since urlopen() returns a stream of bytes rather than a string
def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))   
    with contextlib.closing(urlopen(request_url)) as response:                      
        return response.read().decode('utf-8 ') 


# we are calling main() and we are getting user input by using sys.argv
# We have not limited ourself to only one url as input, 
# instead, we are saying that give us as many urls as you want, 
# we will make them tiny. map() is a simple way of looping
# over a list and passing it to a function one by one.

# def main():                                                                
#     for tinyurl in map(make_tiny, sys.argv[1:]):                    
#         print(tinyurl)

#above function is comment will only provide one url at at time

def main():
    url = 'https://www.geeksforgeeks.org/python-url-shortener-using-tinyurl-api/'
    print(make_tiny(url))  


if __name__ == '__main__':
    main()  