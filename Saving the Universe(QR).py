def totalDamage(commands):
    charge = 1
    total_damage = 0
    for x in commands:
        if x == 'S':
            total_damage += charge
        else:
            charge *= 2
    
    return total_damage

def check(i, commands):
    if commands[i] == 'C' and commands[i+1] == 'S':
        return True
    else:
        return False


def minimize_hacks():
    cases = int(input())
    
    for i in range(cases):
        resistance = int(input())
        commands = list(input())
        flag = 1
        total_damage = totalDamage(commands)
                
   #     print('TOTAL DAMAGE: {} '.format(total_damage))
        
        count = 0
        p = -1
        if 'C' not in commands:
            if len(commands) < resistance:
                   print('Case #{}: 0'.format(i+1))
            else:
                print('Case #{}: IMPOSSIBLE'.format(i+1))
            continue
        
        while(total_damage > resistance):
            
            itr = p + 1
            
            if(itr+1 < len(commands)):
                while (not check(itr, commands)):
                    itr += 1
            else:
                itr = 0
                while (not check(itr, commands)):
                    itr += 1
                
   #         print('BASE: ', commands)
            t = commands[itr]
            commands[itr] = commands[itr+1]
            commands[itr+1] = t
            
    #        print('MODI: ',commands)
            
            p = itr
            count += 1
            total_damage = totalDamage(commands)
        
    #    print('DAMAGE: ',total_damage)
        print('Case #{}: {}'.format(i+1, count))
        
minimize_hacks()
