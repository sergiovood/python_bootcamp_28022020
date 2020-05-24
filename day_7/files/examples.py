# pomocna literatura: https://www.guru99.com/reading-and-writing-files-in-python.html

# try:
#     f = open("data_podstawy_pracy_z_plikami/logs.txt", encoding="CP1251")
#     print(f.read())
#     1 / 0
# except:
#     1 / 0
# finally:
#     print("Zamykam plik")
#     f.close()

# with open("data_podstawy_pracy_z_plikami/logs.txt") as f:
#     with open("data_podstawy_pracy_z_plikami/pan_tadeusz.txt") as pan_t:
#         print(len(pan_t.read()))
#     print(f.read())

# with open("xxx.txt", "w") as f:
#     f.write("Ala ma kota.\n kot ma Alę\n asas\n")

with open("worksplace/day_7/xxx.txt") as f:
    for line in f:
        print(line, end="")
    for line in f.readlines():
        print(line)
