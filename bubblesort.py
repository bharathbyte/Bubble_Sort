#Input

n = int(input("Enter the number of elements in your array"))

print("Enter your array")

array = list(map(int, input().split()))


#Sorting

j = n

while(j>0):

    for i in range(0,j-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp

    j-=1


#Output

for element in array:
    print(element, end= " ")
