import re
String=input("Enter the String:")
Substring=input("Enter the Substring you want to find in the String:")
if re.search(Substring,String):
    print("Yes!!! Subtring '{0}' is present in the String '{1}'".format(Substring,String))
else:
    print("No Subtring '{0}' is not present in the String '{1}'".format(Substring,String))
