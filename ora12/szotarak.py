def beolvas(filepath: str):
    szinek={}
    fileobject = open(filepath, "r")
    for row in fileobject:
        row_datas = row.strip().split("\t")
        szinek[row_datas[1]] = row_datas[3], row_datas[4], row_datas[5]
        fileobject.close
    return szinek

my_str=""
my_list=[]
my_tuple=()
my_dict={}

my_tuple2 = (42,12,76,23,51,23,36)
print(my_tuple2,len(my_tuple2), my_tuple2[4])
my_dict["kulcs"] = "érték"
my_dict["alma"] = "apple"
my_dict["egér"] = "mouse"
print(my_dict)
print(my_dict["alma"])

szin_szotar = beolvas("color.csv")
print(type(szin_szotar["Narancs"]))
print(type(szin_szotar))
print(len(szin_szotar))
print(szin_szotar["Narancs"])
print(szin_szotar.get("kutya", "nincs ilyen szín"))
print("kutya" in szin_szotar)
print(szin_szotar.get("Narancs", "nincs ilyen szín"))
print("kutya" in szin_szotar)
print(szin_szotar.keys())
print(szin_szotar.values())
print(szin_szotar.items())
szin_szotar2 = szin_szotar.copy()
szin_szotar3 = szin_szotar
print(len(szin_szotar),len(szin_szotar2),len(szin_szotar3))
del(szin_szotar2["Narancs"])
print(len(szin_szotar),len(szin_szotar2),len(szin_szotar3))
szin_szotar3.clear()
print(len(szin_szotar),len(szin_szotar2),len(szin_szotar3))