import math




def circ_hitreg(c1, c2) -> bool:
    x1, y1, r1 = c1
    x2, y2, r2 = c2
   
    

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance <= r1+r2:
        return True
    else:
        return False


# Need to test this
def rect_hitreg(r1, r2) -> bool:
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2
    
    if x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
        return True
    else:
        return False


