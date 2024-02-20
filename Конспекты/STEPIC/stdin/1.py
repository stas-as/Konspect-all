from csv import *
def condense_csv(filename, id_name):
    with open(filename, "r", encoding="utf-8") as f, open("condensed.csv", "w", encoding="utf-8") as res:
        rows = list(reader(f))
        w = writer(res)
        head=[id_name] 
        val = [rows[0][0]]
        f = True
        for n, s, z in rows:
            if f:
                if n in val:
                    head.append(s)
                    val.append(z)
                else: 
                    f = False
                    w.writerow(head)
                    w.writerow(val)
                    val = [n]
            else:
                if n in val:
                    val.append(z)
                else:
                    w.writerow(val)
                    val = [n]
                    val.append(z)