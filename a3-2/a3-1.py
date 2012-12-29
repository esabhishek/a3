file_handle = open( "knapsack1.txt", "r" )
str = file_handle.readline()
total_weight = int(str.split()[0])
num_items = int(str.split()[1])

print num_items
print total_weight

knapsack_array = []


for ctr in range(0, num_items + 1):
    for ctr1 in range(0, total_weight + 1):
        temp = []
        knapsack_array.append(temp)

i = 0
for i in range (0, num_items + 1):
    print i
    temp = []
    knapsack_array.append(temp)
    current_val = 0
    if i > 0:
        str = file_handle.readline()
        value  = int(str.split()[0])
        weight = int(str.split()[1])
    for j in range (0, total_weight + 1 ):
        if i == 0:
            current_val = 0
        else:
            
            #print str
            index1 = i - 1
            index2_1 = j
            index2_2 = j - weight
            #print"\n***************************************\n"
            #print j
            #print ""
            #print index1
            #print index2_1
            #print index2_2
            
            current_val = knapsack_array[index1][index2_1]
            if index2_2 >= 0 and current_val < knapsack_array[index1][index2_2] + value:
                current_val = knapsack_array[index1][index2_2] + value
        knapsack_array[i].append(current_val)    
    
    #print knapsack_array[i]
    #print len(knapsack_array[i])
print knapsack_array[num_items]   
print knapsack_array[num_items][total_weight]
        
  