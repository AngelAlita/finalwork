import filecmp

def compare(file1 , file2):
    f1=open(file1)
    f2=open(file2)
    if(filecmp.cmp(file1,file2)):
        return 0
    else:
        str1=f1.read()
        str2=f2.read()
        for i in range(max(len(str1),len(str2))):
            if(str1[i]!=str2[i]):
                return i+1

if __name__=='__main__':
    print("Hello World")
    file1='1.txt'
    file2='2.txt'
    if(compare(file1,file2)==0):
        print("No Difference!")
    else:
        print(compare(file1,file2))
    

