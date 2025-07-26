with open("records.txt","r") as file:
    lines=file.readlines()
    
#print(lines)
sum=0

print("Data = ",end=" ")
for line in lines:
    formated_line= line.rstrip("\n")
    #print(type(new))
    #x= int(new)
    #print(line)
    print(int(formated_line),end=" ")
    sum+=int(formated_line)
    
    
    
mean = sum/len(lines)
print("\nMean = ",mean)
