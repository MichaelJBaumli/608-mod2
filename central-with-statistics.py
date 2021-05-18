#Program Name: central-with-statistics.py
#Assignment Module 2
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210517

import  statistics

statistics.mean

statistics.mode

statistics.median

#Variable
grades = [85,93,45,89,85]



classgrade = statistics.mean(grades)

print("The mean grade for the class is:", classgrade)

mediangrade = statistics.mode(grades)

print("The median grade is: ", mediangrade)

modegrade = statistics.mode(grades)

print("The mode grade is: ",modegrade)