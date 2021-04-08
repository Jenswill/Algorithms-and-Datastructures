

def load_citizen():
  
   
    citizens = int(input())
    try:
        citizenlist_list = [0 for x in range(citizens)]
        citizenlist_list[0] = 1
    except:
        exit()
    return citizenlist_list


def load_m_list(something):
    
    m = int(input())
    m_list = {}
    

    for h in range(m):
        m_input= input().split()
        values = m_input[1:]
        m_list[m_input[0]] = values

    
    return m_list



def main():
    citizen_list = load_citizen()
    m_list = load_m_list(citizen_list)
    isprinted = False
    day = 1
    try:
        queue = m_list[str(0)]
    except:
        exit()
    tempqueue = []
    
    while(len(queue) > 0):
        for i in queue:
            if citizen_list[int(i)] == 0:
                citizen_list[int(i)] = 1
                if not isprinted:
                    print('Day ' + str(day))
                    day +=1
                    isprinted = True
                print(i)
            try:
                tempqueue = tempqueue + m_list[i]
                m_list[i] = []
            except:
                pass
        queue = tempqueue
        tempqueue = []    
        isprinted = False

    

main()


    
    



