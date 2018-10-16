cevap = 0

for a in range(0,101):
    for b in range(0,51):
        for c in range(0,21):
            for d in range(0,11):
                for e in range(0,5):
                    for f in range(0,3):
                        if a+2*b+5*c+10*d+25*e+50*f == 100:
                            cevap += 1
print cevap
