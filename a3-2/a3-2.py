file_handle = open( "knapsack1.txt", "r" )
str = file_handle.readline()
total_weight = int(str.split()[0])
num_items = int(str.split()[1])

print num_items
print total_weight

knapsack_array = [[[]]] * (num_items + 1)
knapsack_array[0] = []
knapsack_array[0].append([0,0])


i = 0

for i in range (0, num_items):
    print i
    
    knapsack_array[1] = []
    current_val = 0
    
    str = file_handle.readline()
    value  = int(str.split()[0])
    weight = int(str.split()[1])
        
   
    for iter in knapsack_array[0]:
        temp = [iter[0] , iter[1]]
        knapsack_array[1].append(temp)
    
    length = len(knapsack_array[0])
    j = 0
    for iter in knapsack_array[0]:
        #j = 0
        if (iter[0] + weight <= total_weight):
            flag = False
            while (j < len (knapsack_array[1]) and iter[0] + weight > knapsack_array[1][j][0] ):
                if (knapsack_array[1][j][1] > iter[1] + value):
                    flag =  True
                    break
                j += 1
            if flag :
                j -= 1
                continue
            
 
            knapsack_array[1].insert(j, [iter[0]  + weight , iter[1] + value])

            latest_value = iter[1] + value
            k = j + 1

            while (k < len(knapsack_array[1])) and knapsack_array[1][k][1] < latest_value and j < len(knapsack_array[1]) :
                 knapsack_array[1].remove(knapsack_array[1][k])

    knapsack_array[0] = knapsack_array[1]                    
       
print knapsack_array[1]
print knapsack_array[1][len(knapsack_array[1]) - 1]
        
  