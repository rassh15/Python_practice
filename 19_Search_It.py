'''
You are given few sentences as a list (Python list of sentences).
Take a query string as a input from the user.
You have to pull out the sentences matching a query inputted by the user
in decreasing order of relevance after converting every word in the query
and sentence to lowercase.
Most relevant sentence is the one with the maximum number of matching words
with the query.

sentences['This is good','python is good','python is not python snake']

Input:
Please input your query string: "Python is"

Output:
3 results found :
1. python is not python snake
2. python is good
3. This is good

'''
import re

sent_list = ['what is python', 'do you know','python in web development',
'python in ML','python in CV', 'python is good and python is easy','understand that woha']

search = 'what'#input("Enter your query: ").lower()
sent_dict = {}

for txt in sent_list:
        
    x = re.findall(search, txt)
    if len(x)!=0: sent_dict[txt] = len(x)

print(f"{len(sent_dict)} results found")

def sort_dict_by_value(d, reverse = False):
      return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

for key in sort_dict_by_value(sent_dict, True).keys():
    print(key)



