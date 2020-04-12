usr_txt = input("Podaj tekst:")
usr_txt = usr_txt.replace(" ", "")
line1 = usr_txt[::2]
line2 = usr_txt[1::2]
margin = " "
line1 = margin.join(line1)
line2 = margin.join(line2)
print(f"""
{line1.upper()} 
{line2.upper()}
 """)
