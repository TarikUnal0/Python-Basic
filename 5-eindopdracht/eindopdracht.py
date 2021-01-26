import time

a = input("Uren:"); a=int(a)
b = input("Minuten:"); b=int(b)
c = input("Secondes:"); c=int(c)
def tijd(a,b,c):
    for h in range(a, 24):
        for m in range(b, 60):
            for s in range(c, 60):
                if h == 23:
                    if m == 59:
                        if s == 59:
                            a=0
                if m == 59:
                    if s == 59:
                        b = 0 
                if s == 59:
                    c = 0 
                klok = f"{h:02}:{m:02}:{s:02}"
                print(klok)
                time.sleep(1)
                       
tijd(a,b,c)
