def witnesses(heights):
    counter = 0
    greater_height = 0

    for index in range(len(heights)-1, -1, -1):
        if heights[index] > greater_height:
            counter += 1         
            greater_height = heights[index]
        
    
    return counter
            



print(witnesses([3,6,3,4,1]))
print(witnesses([9,6,7,1,8]))
print(witnesses([10,11,5,7,15,1,9,9]))
print(witnesses([11,40,5,30,6,28,25,25,26,1,0]))