import numpy as np

data=np.array([59,59,38,60,80,43,78,38,48,58,84,93,83,85,39,19,68,87,79,98])

data_sheet=data.reshape(5,4)
print(f"  s1 s2 s3 s4")
print(data_sheet)

print("marks of 3rd student: ",data_sheet[2,:])
print("marks of subject s3: ", data_sheet[ : ,2])

total=np.sum(data_sheet,axis=1)
print("student 1: ",total[0],"student 2: ",total[1],"student 3: ",total[2],"student 4: ",total[3])
average=np.sum(data_sheet,axis=0)/5
print("s1 average: ",average[0],"s2 average: ",average[1],"s3 average: ",average[2],"s4 average: ",average[3])
for i in range(5):
    student=data_sheet[i:i+1][data_sheet[i:i+1]<40]
    print(f"student{i+1} fail with: ",student)
