from utils import alphabets_list, alphabets_dict
from utils import trim_spaces
import argparse
from iso639 import Lang
from langdetect import detect

language = "English"
iso639_1 = Lang(language).pt1

def cipher(plain_text, key):
    cipher_text = ""
    for alphabet in plain_text:
        if alphabet==" ":
            cipher_text += " "
        else:
            cipher_index = (alphabets_dict[alphabet]+key)%26
            cipher_text += alphabets_list[cipher_index]

    return cipher_text 

def decipher(cipher_text, key):
    plain_text = ""
    for alphabet in cipher_text:
        if alphabet==" ":
            plain_text += " "
        else:
            plain_index = (alphabets_dict[alphabet]-key)%26
            plain_text += alphabets_list[plain_index]
            
    return plain_text



parser = argparse.ArgumentParser()
parser.add_argument("type", type=int, help="Cipher or Decipher")
parser.add_argument("--auto", action="store_true", help="automatically deciphers")
parser.add_argument("-lang", "--lang", type=str, default="False", help="Language to decipher in")

args = parser.parse_args()

if args.type:
    plain_text = input("Enter the plain text : ")
    key = int(input("Enter the key : "))
    print(f"Cipher text : {cipher(plain_text, key)}")
    
else:   
    cipher_text = input("Enter the cipher text : ")
    
    if(args.auto):
        try:
            key = 0
            lang = args.lang.capitalize()
            while(key<26):
                plain_text = decipher(cipher_text, key)
                if(args.lang=="False"):
                    print(f"Key used : {key}")
                    print(f"Plain text : {plain_text}")
                    print("========================================================")
                    
                elif(Lang((detect(plain_text))).pt1 == Lang(lang).pt1):
                    print(f"Plain text : {plain_text}")
                    break
                
                key += 1
                
        except Exception as e:
            print(f"Error : {e}") 
    
    else:            
        key = int(input("Enter the key : "))     
        print(f"Plain text : {decipher(cipher_text, key)}")
