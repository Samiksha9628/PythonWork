def pyramidPattern():
    num=int(input("Enter size of pattern to form pyramid:"))
    for i in range(num):
        for j in range(num-i,0,-1):
            print(end=" ")
        for j in range(0,i+1):
            print(end="* ")
        print("\r")
        
        
pyramidPattern()

def diamondPattern():
    num=int(input("Enter size of pattern to form diamond:")) 
    for i in range(num):
        for j in range(num-i,0,-1):
            print(end=" ")
        for j in range(0,i+1):
            print(end="* ")
        print("\r")
    for i in range(1,num):
        for j in range(0,i+1):
            print(end=" ")
        for j in range(num,i,-1):
            print(end="* ")
        print("\r")

diamondPattern()
        