#Program Name: central-native.py
#Assignment Module 2
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210517


#Variable
grades = [85,93,45,89,85]

#Count Finder
count = len(grades)
print("The count of the grades for the class is: ", count)

#Sum Finder
sumgrade = sum(grades)
print("The sum of the grades for the class is: ",sumgrade)



#Mean Finder
classgrade = sum(grades)/len(grades)

print("The mean grade for the class is: ", classgrade)


#Median Finder
sortedgrades = sorted(grades)

middlegrade = len(grades)//2

print("The median grade is: ", sortedgrades[middlegrade])

#Mode Finder
i = 0
j = 0
modegrade= []
modegradecount=[]
modegrade.append(sortedgrades[i])
modegradecount.append(1)
for x in sortedgrades:
    i = i + 1
    if i >= len(sortedgrades):
        break
    if sortedgrades[i] == sortedgrades[i-1]:
        modegradecount[j] = modegradecount[j]+1
    else:
        modegrade.append(sortedgrades[i])
        modegradecount.append(1)
        j = j + 1
#Yeah, I am proud of this as I built this function entirely on my own.  
#Yes this will not work if there are two or more two values with a max. 
modegradeindex = modegradecount.index(max(modegradecount))

print("The mode grade is: ",modegrade[modegradeindex])
