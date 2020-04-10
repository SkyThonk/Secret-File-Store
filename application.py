import time
import os
import getpass
import random
import shutil

def ClearCmd():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def IntroScreen():
    ClearCmd()
    print('#####################################################################################')
    print('#                                                                                   #')
    print('#                           Welcome to the Secret File                              #')
    print('#                                 Author: Sky                                       #')
    print('#                          Contact: github.com/SkyThonk                             #')
    print('#                                                                                   #')
    print('#####################################################################################')
    time.sleep(3)
    ClearCmd()

def MainMenu():
    print('#####################################################################################')
    print('#                                                                                   #')
    print('#    Enter to Continue                                                              #')
    print('#    1 -> For creating new secret file                                              #')
    print('#    2 -> Access the existing secret file                                           #')
    print('#    3 -> Exit                                                                      #')
    print('#    4 -> About                                                                     #')
    print('#                                                                                   #')
    print('#####################################################################################')
    ans = int(input('Enter: '))
    ClearCmd()
    return ans

def AccessMenu():
    print('#####################################################################################')
    print('#                                                                                   #')
    print('#    Enter to Continue                                                              #')
    print('#    1 -> Get the path of your stored files in Secret Folder                        #')
    print('#    2 -> Move your important files in the Secret Folder                            #')
    print('#    3 -> Secure the Secret Folder                                                  #')
    print('#    4 -> Exit                                                                      #')
    print('#                                                                                   #')
    print('#####################################################################################')
    ans = int(input('Enter: '))
    ClearCmd()
    return ans

def CreateFile():
    Dpath = input("Enter the path where you wanted to create: ")
    Dname = input("Enter the file name: ")
    ClearCmd()
    while True:
        print("Enter Number Password Only")
        while True:
            pin1 = getpass.getpass()
            try:
                pin1 = int(pin1)
                break
            except ValueError:
                ClearCmd()
                print("Password is Not Valid\nEnter Number Password Only")

        ClearCmd()
        print("Please confirm your password again")
        pin2 = getpass.getpass()
        pin2 = int(pin2)
        if pin1==pin2:
            break
        else:
            ClearCmd()
            print("Password did not matched\nRenter again\n")
    ClearCmd()
    try:
        path = os.path.join(Dpath,Dname)
        os.mkdir(path)
        for i in range(101):
            os.mkdir(path+'/'+str(i))
            for j in range(101):
                os.mkdir(path+'/'+str(i)+'/'+str(j))
                for k in range(11):
                    os.mkdir(path+'/'+str(i)+'/'+str(j)+'/'+str(k))
            print("Creating Secret File: {}%".format(i),end="\r")
        FileWrite(pin1,path)
        ClearCmd()
        print("File Successfully Created")
    except FileExistsError:
        print("Not Created")


def FileWrite(pin1,path):
    arr = []
    r1 = random.randrange(1,100,1)
    r2 = random.randrange(1,100,1)
    r3 = random.randrange(1,10,1)
    arr.append(pin1)
    arr.append(r1)
    arr.append(r2)
    arr.append(r3)
    arr.append(7)
    arr= str(arr)
    arr=arr.encode('ascii')
    with open(path+"/55/65/7/config.bin","wb") as f:
        f.write(arr)

def FilterArr(num):
    num2 = str(num)
    num2 = (list(num2[3:-2]))
    num3 = []
    for j in num2:
        if not j == ' ':
            num3.append(j)
    arr = []
    nsum = 0
    for i in num3:
        if not i == ',':
            j = int(i)
            nsum = nsum*10 + j
        else:
            arr.append(nsum)
            nsum = 0
    return arr
    
def AssesFile():
    path = input("Enter the path of Secret File: ")

    while True:
        try:
            with open(path+"/55/65/7/config.bin","rb") as f:
                num = f.read()
            break
        except FileNotFoundError:
            ClearCmd()
            print("Entered Path is Wrong or It's Not Secret File\n")
            path = input("Enter again the currect path of Secret File: ")
    arr = FilterArr(num)
    while True:
        try:
            print('Enter the Password to access the folder')
            passw = getpass.getpass()
            passw = int(passw)
            if(arr[0]==passw):
                ClearCmd()
                options2 = AccessMenu()
                AccessOptionSelection(options2,path,passw)
                break
            else:
                ClearCmd()
                print("Entered Password is Incorret\nPlease Renter the Password\n")
        except ValueError:
            ClearCmd()
            print("Entered Password is not Valid\nPlease Renter the Password\n")

def getLocation(path):
    with open(path+"/55/65/7/config.bin","rb") as f:
        num = f.read()
    arr = FilterArr(num)
    location = os.path.join(path,str(arr[1]),str(arr[2]),str(arr[3]))
    return location

def pathShow(path):
    print("You can get your stored files by visiting the following path in the File Explorer: ",end=' ')
    loc = getLocation(path)
    print(loc)
    print("\n\nPlease make sure that you secure the file by running this program again\nHint: Run the Program->2->3")

def MoveFile(path):
    while True:
        try:
            userPath = input("Enter the path of the file which you wanted to move in secret file: ")
            docPath = getLocation(path)
            shutil.move(userPath,docPath)
            print("\nFile Sucessfully Moved")
            print("\n\nThank you for using the program")
            break
        except FileNotFoundError:
            ClearCmd()
            print("Entered Path dosen't exit\n")

def SecureFile(path,passw):
    currentPath = getLocation(path)
    FileWrite(passw,path)
    newPath = getLocation(path)
    print("File is securing .......")
    for r, d, f in os.walk(currentPath):
        for file in f:
            moveFile = os.path.join(currentPath,file)
            shutil.move(moveFile,newPath)
    print("\nSucessfully Secured")
    print("\n\nThank you for using the program")

def AccessOptionSelection(options2,path,passw):
    if options2 == 1:
        ClearCmd()
        pathShow(path)
    elif options2 == 2:
        MoveFile(path)
    elif options2 == 3:
        SecureFile(path,passw)
    elif options2 == 4:
        print("Thank you for using this program\nSuccessfully Exit")
    else:
        print("You have Enter Wrong Input")
        options2 = AccessMenu()
        AccessOptionSelection(options2,path,passw)

def About():
    print("Author:      Sky\n")
    print("Contact:     github.com/SkyThonk\n")
    print("Repository:  https://github.com/SkyThonk/Secret-File-Store\n")
    print("Description: This is an automation script that can create 100 x 100 x 10 nested folders in your pc ") 
    print("             and randomly it stores your important file which makes it very hard to find that files")
    print("             and to get the location of your stored file you require a password.\n")

def optionSelection(options):
    if options == 1:
        CreateFile()
    elif options == 2:
        AssesFile()
    elif options == 3:
        print("Thank you for using this program\nSuccessfully Exit")
    elif options == 4:
        About()
    else:
        print("You have Enter Wrong Input")
        options = MainMenu()
        optionSelection(options)


if __name__ == "__main__":
    IntroScreen()
    options=MainMenu()
    optionSelection(options)

    