import sys
sys.setrecursionlimit(11000)
def load_citizen():
  
   
    citizens = int(input())
    try:
        citizenlist_list = [-1 for x in range(citizens)]
    except:
        exit()
    return citizenlist_list


def load_m_list():
    
    m = int(input())
    m_list = {}
    

    for h in range(m):
        m_input= input().split()
        try:
            m_list[m_input[0]] = (m_list[m_input[0]] + [m_input[1]])
        except:
            m_list[m_input[0]] = [m_input[1]]
        try:
            m_list[m_input[1]] = m_list[m_input[1]] + [m_input[0]]
        except:
            m_list[m_input[1]] =  [m_input[0]]



    return m_list


def sortEnemies(index,player,m_list,playerlist,teams):
    
    teams[str(index)].append(player)
    playerlist[player] = index
    try:
        for enemy in m_list[str(player)]:
            if playerlist[int(enemy)] == -1:
                playerlist,teams = sortEnemies((index+1)%2,int(enemy),m_list,playerlist,teams)
            elif playerlist[int(enemy)] == index:
               print('NO')
               exit()

    except KeyError:
        pass
    except:
        exit()
    return playerlist,teams

def main():
    playerlist = load_citizen()
    
    m_list = load_m_list()
    
    teams = {'0':[],'1':[]}

    

    for player in range(len(playerlist)):
        if playerlist[player] == -1:
            playerlist,teams = sortEnemies(1,player,m_list,playerlist,teams)
    
    team1 = teams['0']
    team2 = teams['1']
    if len(team1) == len(playerlist) and len(playerlist) > 1:
        team2.append(team1[-1])
        team1.pop()
    elif len(team2) == len(playerlist) and len(playerlist) > 1:
        team1.append(team2[-1])
        team2.pop()
    elif len(playerlist) < 2:
        print('NO')
        exit()
    team1.sort()
    team2.sort()
    print(*team1)
    print(*team2)

main()