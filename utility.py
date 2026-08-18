import math

def circ_hitreg(c1, c2) -> bool:
    x1, y1, r1 = c1
    x2, y2, r2 = c2
   
    

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance <= r1+r2:
        return True
    else:
        return False



