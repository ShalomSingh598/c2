numlarge=int(input("Enter the largest number: "))
numsmall=int(input("Enter the smallest number: "))
while numsmall:
    numberstore=numsmall
    numsmall=numlarge%numsmall
    numlarge=numberstore

print("HCF IS:",numlarge)