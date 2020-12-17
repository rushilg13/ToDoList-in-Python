class Todo:
    def __init__(self):
        self.to_list = {}

    def size(self):
        return (len(self.to_list))

    def add(self, text):
        self.to_list[len(self.to_list)] = [text, False]
        print("Added Todo:", text)

    def show(self):
        show_list={}
        for i in self.to_list.keys():
            if self.to_list[i][1]==False:
                show_list[i]=self.to_list[i][0]

        for i in show_list:
            print("[",i, "]", show_list[i])
    
    def report(self):
        count_false=0
        for i in self.to_list.values():
            if i[1]==False:
                count_false+=1
        print("Pending", count_false)
        print("Completed", len(self.to_list)-count_false)

    def del_num(self, n):
        del self.to_list[n]
        print("Deleted Todo #", end="")
        print(n)

    def help_user(self):
        pass

    def done(self, n):
        self.to_list[n][1]=True
        print("Marked #", end="")
        print(n, "as Done!")
    
    def exit_sys(self):
        exit()

todo = Todo()

ch=''
while(ch!="End"):
    print("add Add a new Todo")
    print("ls Show Remaining Todos")
    print("del NUMBER Delete a Todo")
    print("done NUMBER Complete a Todo")
    print("help Show Usage")
    print("report Show Statistics")
    print("exit")
    ch=str(input())
    if(ch=='add'):
        s=str(input("Enter new Todo\n"))
        todo.add(s)
    elif(ch=='ls'):
        todo.show()
    elif(ch=='del'):
        n=int(input("Enter index to delete\n"))
        todo.del_num(n)
    elif(ch=='exit'):
        exit()
    elif(ch=='done'):
        n=int(input("Enter index to mark as done\n"))
        todo.done(n)
    elif(ch=='help'):
        print("add Add a new Todo")
        print("ls Show Remaining Todos")
        print("del NUMBER Delete a Todo")
        print("done NUMBER Complete a Todo")
        print("help Show Usage")
        print("report Show Statistics")
        print("exit")
    elif(ch=='report'):
        todo.report()
    else:
        print("Wrong Command")
