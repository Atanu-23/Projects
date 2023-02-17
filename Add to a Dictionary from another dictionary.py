dict1={'key 1':'Hello','key 2':'World'}
dict2={'key 3':'How','key 4':'Are','key 5':'You'}
print("Initially Dictionaries are:"+str(dict1)+"and"+str(dict2))
dict1.update(dict2)
dict1.update(Newkey='!!!')
print("New Dictionary is:",dict1)
