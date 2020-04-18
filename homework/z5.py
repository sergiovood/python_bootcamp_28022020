usr_txt = input("Wprowadz dowolny tekst:")
lenght = "*"*(len(usr_txt)+4)
result = f"""
{lenght}
* {usr_txt} *
{lenght}
"""
print(result)