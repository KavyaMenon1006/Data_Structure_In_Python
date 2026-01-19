class Node:
  def _init_(self,data=none,next=None)
  self.data=data
  self.next=next
class Linked_list:
  def _init_(self):
    self.head=None
  def insert_at_beginning(self,data):
    node=Node(data,self.head)
    self.head=node
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
      itr=self.head
    while itr:
      llstr+=str(itr.data)+'-->'
      itr=itr.next
    print(llstr)
  def insert_values(self,data_list):
    self.head=None
    for data in data_list:
      self.insert_at_end(data)
  def get_length(self):
    count=0
    itr=self.head
    while itr:
      count+=1
      itr=itr.next
    return count
  def remove_at(self,indeddx):
    if index<0 or index>=self.get_length():
      raise exception("Invalid index")
      if index==0:
        self.head=self.head.next
        return
    count=0
    itr=self.head
    while itr:
      if count==index-1:
        itr.next=itr.next.next
        break
      itr=itr.next
      count+=1
  def insert_at(self,index,data):
    if index<0 or index>self.get_length():
      raise exception("Invalid index")
    if index=0:
      self.insert_at_beginning(data)
      return
    count=0
    itr=self.head
    while itr:
      itr=itr.next
      count+=1
