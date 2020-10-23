import sys
import re
n=input()
if(re.match('[0-9]{2}[A-Za-z]{3}[0-9]{4}',n)):
   print("valid")
else:
    print("invalid")

    
    
