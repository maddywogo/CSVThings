# main.py

from utilsPackage.utils import *

# Call the function and store what it returns 
#  in a variable called data
if __name__ == "__main__":
    data = read_CSV_file()
    print("# of rows in dataset:", len(data))
    print("first row in data:",(data[0]))
    print("last row in data:",(data[-1]))
    # I want a list comprehension expression to pull out all the collision types into a set
    #Modify this expression to exclude the blank collision type  ----> condition statement
    collisionTypes = {myData[6] for myData in data}
    print("# of collision type:"), len(collisionTypes)
    print(collisionTypes)
    