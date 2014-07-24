'''
Created on 5 jun. 2014

@author: niels
'''

class Iterator:
    """
    this is my attempt in creating an iterator.
    """

    def __init__(self):
        """ here you can throw a type into the iterator and will return a list sequence of the elements """
        self.typeOfIteration = None
        self.returnValue = None



    def StringIterator(self):
        """ iterate through a string and returns a list of elements from the string"""
        returnlist = []
        if len(self.typeOfIteration) > 0:

            for item in self.typeOfIteration:
                returnlist.append(item)
            if  len(returnlist) == len(self.typeOfIteration):
                return returnlist
        else:
            return "the item given is not iterable"

    def DictIterator(self):
        """ this returns the keys and the  """
        keys1 = []
        valuesl = []
        for key in self.typeOfIteration:

            keys1.append(key)
            valuesl.append(self.typeOfIteration[key])

        return [keys1,valuesl]

    def IntIterator(self):
        """ this is a bad idea """
        intlist = []
        for place in str(self.typeOfIteration):
            intlist.append(int(place))
        return intlist

    def ReturnIteration(self, iterationtype):
        """ this returns the value we want """
        self.typeOfIteration = iterationtype
        self.ret = None

        typedict = {str:self.StringIterator, dict:self.DictIterator, int:self.IntIterator}

#         if len(iterationtype) > 0:

        if self.typeOfIteration != None:
            try:
                return typedict[type(self.typeOfIteration)]()
            except:
                return "type not implemented yet"

if __name__ == '__main__':
    it = Iterator()
    print(it.ReturnIteration(13))
