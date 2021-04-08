def load_input():
    amount = int(input())
    input_list = []
    for i in range(amount):
        command = int(input())
        input_list.append(command)
    return input_list


def main(data):
    counter = 0
    counter_highest = 0
    index_start = -1
    index_out = -1

    for i in range(1, len(data)):

        
        
        if data[i] > data[i-1]:
            counter = 1
            index_start = i
        elif counter != 0 and index_start != -1 and data[i] == data[i-1]: 
                counter = counter + 1    
        elif counter != 0 and index_start != -1 and data[i] < data[i-1]:
            if counter > counter_highest:
                counter_highest = counter
                index_out = index_start
            index_start =-1
            counter = 0
        else:  
            index_start = -1  
            counter = 0   
            
    return index_out, counter_highest




data = load_input()
output1, output2 = main(data)
print(output1)
print(output2)
