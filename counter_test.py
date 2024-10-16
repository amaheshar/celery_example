# from collections import Counter 
  
# # With sequence of items  
# print(Counter(['B','B','A','B','C','A','B',
#                'B','A','C']))
  
# # with dictionary 
# print(Counter({'A':'aa', 'B':'uu', 'C':'jj'}))
  
# # with keyword arguments 
# print(Counter(A=3, B=5, C=2))

# Python program to demonstrate 
# defaultdict 
  
  
# from collections import defaultdict 
  
  
# # Defining a dict 
# d = defaultdict(dict) 
  
# for i in range(5): 
#     d[i] = { 'i': i}
      
# print("Dictionary with values as list:") 
# print(d[8]) 

# Python program to demonstrate 
# ChainMap 
   
   
from collections import ChainMap 
   
   
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'a': 5, 'f': 6}

# Defining the chainmap 
c = ChainMap(d1, d2, d3) 
   
# Accessing Values using key name
print(c['a'])

# Accessing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())
