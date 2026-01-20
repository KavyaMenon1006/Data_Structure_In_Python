def Get_Hash(key):
  h=0
  for char in key:
    h+=ord(char)
  return h%100
'''Implementing hash table'''
class Hash_Table:
  def __init__(self):
    self.Max=100
    self.arr=[None for i in range(self.Max)]
  def get_hash(self,key):
    h=0
    for char in key:
      h+=ord(char)
    return h%self.Max
  '''If we want to add a ke value pair to hash table'''
  def add(self,key,value):
    h=self.get_hash(key)
    '''To add key value pair'''
    self.arr[h]=value
  def get(self,key):
        h=self.get_hash(key)
        return self.arr[h]
  def delete(self,key):
        h=self.get_hash(key)
        self.arr[h]=None
 
'''Input'''
Hash= Hash_Table()
Hash.add("name", "Kavya")
Hash.add("lang", "Python")
print(Hash.get("name"))   
print(Hash.get("lang"))   
Hash.delete("name")
print(Hash.get("name")) 
