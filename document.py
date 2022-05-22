# Put your code below:
fileName = input("Enter the input file name: ")
data = open(fileName, 'r') 
ray = list(data)
#data = file.read()
A = 0
def unexpectedIndices():
     for line in data:
        A += 1
        print(line)
for line in ray:
        A += 1    
print("The file has " + str(A) + " lines")
lineNumbers = input("Enter the line number to display or press zero for full file: ")
if lineNumbers.isdigit():
 LineNumber= int(lineNumbers)
 if A < LineNumber:
    unexpectedIndices()
 else:
  if lineNumbers != 0:
     LineNumber -= 1
     print(ray[LineNumber])
lineNumbers = input("Enter the line number to display or press zero for full file: ")
if lineNumbers.isdigit():
        if lineNumbers != 0:
             LineNumber= int(lineNumbers)
             LineNumber -= 1
             print(ray[LineNumber])

                
# else:

#     print("The file has " + str(A) + " lines")
       
 
