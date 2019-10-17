import math

def solve_triangle(a=None,b=None,c=None,A=None,B=None,C=None, decimals=16, right_triangle=True):
    if a == 0: a = None
    if b == 0: b = None
    if c == 0: c = None
    if A == 0: A = None
    if B == 0: B = None
    if C == 0: C = None
    if not A == None and A == 90:
        right_triangle = True
    elif not B == None and B == 90:
        right_triangle = True
    elif not C == None and C == 90:
        right_triangle = True

    #try:
    if right_triangle: #is a right triangle
        if A == 90:
            A = C
            C = 90

        elif B == 90:
            B = C
            C = 90
        C = 90
        #conditions: SS, AA, SA (for AA all sides are normalized)

        if A == None and B == None: #SS (two sides)
            if not a == None:
                if not b == None: # side a and b exist
                    print("yess")                       
                    c = (a ** 2 + b ** 2) ** 0.5
                    A = math.degrees(math.atan(a/b))
                    B = math.degrees(math.atan(b/a))
                elif not c == None: # side a and c exist
                    b = (c ** 2 - a ** 2)  ** 0.5
                    A = math.degrees(math.asin(a/c))
                    B = math.degrees(math.acos(a/c))
            elif not b == None:
                if not a == None:
                    c = ((a**2)+(b**2))**0.5
                    A = math.degrees(math.atan(a/b))
                    B = math.degrees(math.atan(b/a))
                elif not c == None:
                    a = ((c**2) - (b**2))**0.5
                    A = math.degrees(math.acos(b/c))
                    B = math.degrees(math.asin(b/c))
            elif not c == None:
                if not a == None:
                    b = (c**2 - a**2) ** 0.5
                    A = math.degrees(math.asin(a/c))
                    B = math.degrees(math.acos(a/c))
                elif not b == None:
                    a = (c**2 - b**2) ** 0.5
                    A = math.degrees(math.acos(b/c))
                    B = math.degrees(math.asin(b/c))
                
        elif a == None and b == None and c == None: #AA (two angles. sides must be normalized)
            pass
        else: #SA (side angle)
            
            if not a == None:
                if not A == None:
                    b = a / math.tan(math.radians(A))
                    print(a, A, b)
                    c = a / (math.sin(math.radians(A)))
                    B = C - A
                elif not B == None:
                    b = a / math.tan(math.radians(B))
                    c = a / math.sin(math.radians(B))
                    A = C - B
            elif not b == None:
                if not A == None:
                    a = b * math.tan(math.radians(A))
                    c = b / math.cos(math.radians(A))
                    B = C - A
                elif not B == None:
                    a = b / math.tan(math.radians(B))
                    c = b / math.sin(math.radians(B))
                    A = C - B
            elif not c == None:
                if not A == None:
                    a = c * math.sin(math.radians(A))
                    b = c * math.cos(math.radians(A))
                    B = C - A
                elif not B == None:
                    a = c * math.cos(math.radians(B))
                    b = c * math.sin(math.radians(B))
                    A = C - B

    else: #None Right Triangle
        pass

    #except Exception as e:
        #return e
    if decimals == 0:
        a,b,c,A,B,C = int(round(a, 0)), int(round(b, 0)), int(round(c, 0)), int(round(A, 0)), int(round(B, 0)), int(round(C, 0))
    else:
        a,b,c,A,B,C = float(round(a, decimals)), float(round(b, decimals)), float(round(c, decimals)), float(round(A, decimals)), float(round(B, decimals)), float(round(C, decimals))

    return [a,b,c,A,B,C]

#print(solve_triangle(3.0,4.0))
print(3/math.tan(math.radians(36.86989764584402)))