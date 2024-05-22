def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8")  # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()
    return

# ierakstit("Marta, ")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()
    return

# pierakstit_klat("Es esmu programmēšanas skolotāja")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

# print(nolasit_visu())

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()

    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()

    return rindas


# saraksts = dabut_rindinas()
# print(saraksts)

# ierakstit("Anna, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcCG4898FTkK5IUBMpLleBHtjK3jUILS3YsjCFfLr56g&s")
# pierakstit_klat("Katls, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtv-3G97RDAt-sgNqxhaEB4f2SDwVxJaOq7JOY0D_7zA&s")
# pierakstit_klat("Kartupelis, https://www.darzaabc.lv/public/assets/images/products/Agrimatco/kartupe%C4%BCi/kartupeli-monalisa-dzeltenie-seklas-kartupelu-stadamais-materials.jpg")

print(dabut_rindinas())