def dot_product(list1,list2):
    list1 = map(int,list1.split(","))
    list2 = map(int, list2.split(","))
    if len(x) > len (y) or len(y) > len(x):
        answer = float("NaN")
    else:
        answer = sum(a*b for a,b in zip(list1, list2))
    return answer
x=input("Write the coordinates of the first vector, separate the numbers with commas: ")
y=input("Write the coordinates of the second vector, separate the numbers with commas: ")

print (("The dot product is: ")+ str(dot_product(x,y)))
