# Python Function Parameters
# When a final formal parameter of the form **name is present, 
# it receives a dictionary (Mapping Types — dict) containing all keyword arguments 
# except for those corresponding to a formal parameter. 
# This may be combined with a formal parameter of the form *name which receives a 
# tuple containing the positional arguments beyond the formal parameter list. 
# (*name must occur before **name.) For Example;

def cheeseshop(kind, *arguments, **keywords):
   print("-- Do you have any", kind, "?")
   print("-- I'm sorry, we're all out of", kind)

     for arg in arguments:
      print(arg)
      print("-" * 40)


     for kw in keywords:
       print(kw, ":", keywords[kw])
