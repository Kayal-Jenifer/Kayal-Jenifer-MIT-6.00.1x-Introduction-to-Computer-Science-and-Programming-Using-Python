# Write a function to flatten a list. The list contains other lists, strings, or ints.
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

aList=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten(aList):
    if isinstance(aList,list):
        f=[]
        for i in aList:
            f.extend(flatten(i))
        return f
    else:
        return [aList]
        
print(flatten(aList))
    