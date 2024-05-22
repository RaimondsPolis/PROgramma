
def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez=sk1*sk2
    else:
        rez=sk1+sk2
    return rez

for skaitlis in range(1, 11):
    print("mūsu skaitlis:", skaitlis, "rezultāts:",rezultats(4,skaitlis))

skaitlis1=3
skaitlis2=4
print("pirmais skaitlis:",skaitlis1)
print("otrais skaitlis:",skaitlis2)
print("rezultats:",rezultats(skaitlis1,skaitlis2))
