def CN(n,m):
    if(m==0):
        return False
    else:
        qt = n/m
        closest = qt*m
        return closest
    

print(CN(-6,39))