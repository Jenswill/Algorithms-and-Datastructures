
def main():
    amount = int(input())
    

    int_list = []
    stack_list = []
    minFirst_list = []
    isQ = True
    isStack = True
    isMinQ = True

    for index in range(amount):

        command = input().split()
        command_var = command[0]
        int_var = int(command[1])

        if command_var == 'I' and (len(int_list) + 1) < amount:
           
            int_list.append(int_var)
            stack_list.append(int_var)
            
        elif command_var == 'E':
            try:     
                if int_list.index(int_var) == 0 and isQ == True:
                    isQ = True
                else:
                    isQ = False

                if int_var == stack_list[-1] and isStack == True:
                    isStack = True
                    stack_list.pop(-1)
                else:
                    isStack = False

                minFirst_list = int_list.copy()
                minFirst_list.sort()

                if int_var == minFirst_list[0] and isMinQ == True:
                    isMinQ = True
                else:
                    isMinQ = False
            except:
                print('F')



        
    if isQ:
        print('YES')
    else:
        print('NO')

    if isStack:
        print('YES')
    else:
        print('NO')
    
    if isMinQ:
        print('YES')
    else:
        print('NO')



            

    
    


main()
