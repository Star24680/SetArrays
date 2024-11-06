import array as arr
A=arr.array('I',[1,3,5,3,7,9,3])
print("Original Array: " +str(A))
print("Number of occurence of 3 in array: " +str(A.count(3)))
A.reverse()
print("Reverse order of items: " +str(A))