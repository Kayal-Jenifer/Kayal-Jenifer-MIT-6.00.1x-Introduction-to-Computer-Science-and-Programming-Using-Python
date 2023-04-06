# Implement the class myDict with the methods below, which will represent a dictionary without using a dictionary object. 
# The methods you implement below should have the same behavior as a dict object, including raising appropriate exceptions.
# Your code does not have to be efficient. Any code that uses a Python dictionary object will receive 0.

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
# Your code here...

class myDict(object):
    def __init__(self):
        self.dictionary = []

    def assign(self, k, v):
        self.k = k
        self.v = v
        isThere = False
        if len(self.dictionary) == 0:
            self.dictionary += [[k, v]]
            isThere = True

        for item in self.dictionary:
            if k == item[0]:
                item[1] = v
                isThere = True

        if isThere == False:
            self.dictionary += [[k, v]]

    def getval(self, k):
        for item in self.dictionary:
                if item[0] == k:
                    return item[1]
        raise KeyError

    def delete(self, k):
  
        count = False
        for item in self.dictionary:
            if k == item[0]:
                del item[:]
                self.dictionary = [x for x in self.dictionary if x != []]
                count = True
        if count == False:
            raise KeyError




