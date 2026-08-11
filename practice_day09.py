import numpy as np

marks=np.array([83,39,95,67,89,81,74,28,90,52,20,63])
print(marks)

print ("3rd student: ", marks[2])
print(marks[:5])

pass_marks=marks[marks>=50]
print(pass_marks)

arr=np.sort(marks)
print("sorted array: ",arr)

print(np.where(marks==20))


print (marks.shape)
new_arr=marks.reshape(3,4)
print(new_arr,new_arr.shape)

cop=marks.copy()
cop[0]=0
print("copy:",cop)
print("original: ", marks)
viw=marks.view()
viw[0]=1
print("view: ",viw)
print("original: ", marks)
