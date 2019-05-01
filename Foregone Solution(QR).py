
def foregone():
    cases = int(input())
    
    for i in range(cases):
        s = list(input())
        other = ""
        
        for j in range(len(s)):
            if(s[j] == "4"):
                s[j] = "3"
                other += "1"
                continue
            other += "0"
            
        other = list(other)
        for j in range(len(other)):
            if(other[j] == "0"):
                other.pop(j)
            if(other[j] == "1"):
                break
        other = ''.join(other)
        s = ''.join(s)
        pr3int('CASE #{}: {} {}'.format(i+1, s, other))

foregone()
