"""
My very own cipher that I developed for the sole purpose of having fun, not to make it too complicated and not to make it too easy.
It has 144 possibilities of keys.
"""

from utils import alphabets_dict
from utils import alphabets_list


def fix_key(h, m):
    h = h%12
    m = m%60
    m = m//5
    return h, m



def decrypt(char, h, m, hosc, mosc):

    index = alphabets_dict.get(char, -1)  
    
    if index == -1:
        return char, 'nothing'  

    if index < 12:  
        if hosc:
            i = (index + h) % 12
        else:
            i = (index - h + 12) % 12

        return alphabets_list[i], 'hosc'

    elif 12 <= index < 24:  
        if mosc:
            i = (index + m) % 24
            if i < 12:
                i += 12  
        else:
            check = index - m
            if check == 0 or check == 12:
                return char, 'mosc'
            elif check < 12:
                i = check + 12
            else:
                i = check

        return alphabets_list[i], 'mosc'

    elif char in ('y', 'z'):  
        return 'z' if char == 'y' else 'y', 'nothing'

    return char, 'nothing'


def encrypt(char, h, m, hosc, mosc):

    index = alphabets_dict.get(char, -1)  
    
    if index == -1:
        return char, 'nothing'  

    if index < 12:  
        if hosc:
            i = (index + h) % 12
        else:
            i = (index - h + 12) % 12

        return alphabets_list[i], 'hosc'

    elif 12 <= index < 24:  
        if mosc:
            i = (index + m) % 24
            if i < 12:
                i += 12  
        else:
            check = index - m
            if check == 0 or check == 12:
                return 'm', 'mosc'
            elif check < 12:
                i = check + 12
            else:
                i = check

        return alphabets_list[i], 'mosc'

    elif char in ('y', 'z'):  
        return 'z' if char == 'y' else 'y', 'nothing'

    return char, 'nothing'




def main():
    text = input("Enter the plain text : ")
    h = int(input("Enter the h key : "))
    m = int(input("Enter the m key : "))

    h, m = fix_key(h, m)

    choice = input("(e)ncrypt or (d)ecrypt : ")
    if choice == 'e':
        hosc, mosc = True, True      
        cipher_text = ""

        for char in text:
            if(char==" "):
                cipher_text += char
            else:
                text, toggle = encrypt(char.lower(), h, m, hosc, mosc)
                cipher_text += text
                if toggle=='mosc': mosc = not(mosc) 
                elif toggle=='hosc': hosc = not(hosc)
        
        print(f"Cipher : {cipher_text}")

    elif choice == 'd':
        hosc, mosc = False, False
        cipher_text = ""

        for char in text:
            if(char==" "):
                cipher_text += char
            else:
                text, toggle = encrypt(char.lower(), h, m, hosc, mosc)
                cipher_text += text
                if toggle=='mosc': mosc = not(mosc) 
                elif toggle=='hosc': hosc = not(hosc)

        print(f"Plain : {cipher_text}")




if __name__ == "__main__":
    main()
