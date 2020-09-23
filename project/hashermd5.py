""""The program to convert string to md5 hashed string.The program also takes various datatypes"""
import hashlib
class Hasher:
    """"The  class to initiate the object which will contain the data to be encoded as values"""
    def __init__(self,tobehashed):
        nlist=[]
        if isinstance(tobehashed,str):
            self.tobehashed=tobehashed
        elif isinstance(tobehashed,dict):
            for key,values in tobehashed.items():
                nlist.append(tobehashed[key])
            if all(isinstance(i,str) for i in nlist):
                self.tobehashed=tobehashed
            else:
                raise ValueError("The values of the dictionary must be a string")
        elif isinstance(tobehashed,list):
            if all(isinstance(i,str) for i in tobehashed):
                self.tobehashed=tobehashed
            else:
                raise ValueError("All the elements of the list must be strings")
        elif isinstance(tobehashed,tuple):
            if all(isinstance(i,str) for i in tobehashed):
                self.tobehashed=tobehashed
            else:
                raise ValueError("All the elements of the tuples must be string")
        else:
            raise TypeError("Out of the recognised types")

    def hashermd5(self):
        """"funtion to do the actual conversion and return the value"""
        newlist=[]
        if isinstance(self.tobehashed,str):
            return hashlib.md5(self.tobehashed.encode()).hexdigest()
        elif isinstance(self.tobehashed,dict):
            for key,value in self.tobehashed.items():
                self.tobehashed[key]= hashlib.md5(value.encode()).hexdigest()
            return self.tobehashed
        elif isinstance(self.tobehashed,list):
            for i in self.tobehashed:
                newlist.append(hashlib.md5(i.encode()).hexdigest())
            return newlist
        elif isinstance(self.tobehashed,tuple):
            for i in self.tobehashed:
                newlist.append(hashlib.md5(i.encode()).hexdigest())
            return newlist
        else:
            raise TypeError("Out of the recognised types")