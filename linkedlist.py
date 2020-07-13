class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class singleLinkedList:
    def __init__(self):
        self.start=None

    def display(self):
        if self.start is None:
            print("List is empty")
            return
        p=self.start
        while p is not None:
            print(p.info,"=>",end='')
            p=p.link
        print()

    def insert_beginning(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp

    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

    def insert_after(self,data,x):
        temp=Node(data)
        if self.start is None:
            print("List is empty")
            return
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        temp.link=p.link
        p.link=temp

    def insert_before(self,data,x):
        temp=Node(data)
        if self.start is None:
            print("List is empty")
            return
        if self.start.info==x:
            temp.link=self.start
            self.start=temp
            return
        p=self.start
        while p is not None:
            if p.link.info==x:
                break
            p=p.link
        temp.link=p.link
        p.link=temp

    def delete_node(self,x):
        if self.start is None:
            print("List is empty")
            return
       
        if self.start.info==x:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        if p.link is None:
            print(x,"not present in the list")
        else:
            p.link=p.link.link

    def delete_start(self):
        if self.start is None:
            print("List is empty")
            return
        self.start=self.start.link

    def delete_end(self):
        if self.start is None:
            print("List is empty")
            return
        if self.start.link is None:
            self.start=None
            return
        p=self.start
        while p.link.link is not None:
            p=p.link
        p.link=None

    def reverse(self):
        prev=None
        p=self.start
        while p is not None:
            Next=p.link
            p.link=prev
            prev=p
            p=Next
        self.start=prev

    def search(self,x):
        if self.start is None:
            print("List is empty")
            return
        p=self.start
        k=0
        while p is not None:
            if p.info==x:
                print(x,"present in the list at position",k)
                return True
            k+=1
            p=p.link
        else:
            print(x,"not present inthe list")
            return False
    def count(self):
        p=self.start
        c=0
        while p is not None:
            c+=1
            p=p.link
        print("Number of nodes present in the list are: ",c)

    def bubble_sort(self):
        end=None
        while end!=self.start.link:
            p=self.start
            while p.link!=end:
                q=p.link
                if p.info>q.info:
                    p.info,q.info=q.info,p.info
                p=p.link
            end=p
                    
        

    def create_list(self):
        n=int(int(input("ENter the number of nodes: ")))
        if n==0:
            return
        for i in range(n):
            data=int(input("ENter the data: "))
            self.insert_at_end(data)
        print()

    
        

list=singleLinkedList()
list.create_list()
while True:
    print("1.Display")
    print("2.Insert beginning")
    print("3.Insert at end")
    print("4.Insert after")
    print("5.Insert before")
    print("6.Delete")
    print("7.Delete starting")
    print("8.Delete end")
    print("9.Reverse")
    print("10.Search")
    print("11.Count")
    print("12.Bubble sort")
    print("17.Quit")
    
    choice=int(input("ENter the choice: "))
    if choice==1:
        list.display()
    elif choice==2:
        x=int(input("ENter the data to be inserted: "))
        list.insert_beginning(x)
    elif choice==3:
        x=int(input("ENter the data to be inserted: "))
        list.insert_at_end(x)
    elif choice==4:
        x=int(input("ENter the data to be inserted: "))
        p=int(input("Enter teh position after: "))
        list.insert_after(x,p)
    elif choice==5:
        x=int(input("ENter the data to be inserted: "))
        p=int(input("Enter teh position after: "))
        list.insert_before(x,p)
    elif choice==6:
        x=int(input("ENter the data to be inserted: "))
        list.delete_node(x)
    elif choice==7:
        list.delete_start()
    elif choice==8:
        list.delete_end()
    elif choice==9:
        list.reverse()
    elif choice==10:
        x=int(input("ENter the data to be searched: "))
        list.search(x)
    elif choice==11:
        list.count()
    elif choice==12:
        list.bubble_sort()

        
    
