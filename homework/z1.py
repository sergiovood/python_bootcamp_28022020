usr_txt = input("Podaj tekst:").replace(" ", "")
line1 = " ".join(usr_txt[::2]).upper()
line2 = " ".join(usr_txt[1::2]).upper()
print(f"""
{line1} 
{line2}
 """)