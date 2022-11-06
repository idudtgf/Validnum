import requests
import colorama
from colorama import Fore , Back , Style
from datetime import datetime
from time import sleep
colorama.init()
import time
time.sleep(0.5)
print(Fore.RED+"[!] "+ Fore.YELLOW+"Welcom to Saidos Tools")
time.sleep(1)
print("")
print( Fore.GREEN+"Please Wait...")
time.sleep(2)

print(Fore.GREEN+""""
      
██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░███╗░░██╗██╗░░░██╗███╗░░░███╗
██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗████╗░██║██║░░░██║████╗░████║
╚██╗░██╔╝███████║██║░░░░░██║██║░░██║██╔██╗██║██║░░░██║██╔████╔██║
░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║██║╚████║██║░░░██║██║╚██╔╝██║
░░╚██╔╝░░██║░░██║███████╗██║██████╔╝██║░╚███║╚██████╔╝██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝

-------------------------------By @SaidosHits---------------------------                                                                                                                                                                                                                                                               
""")
time.sleep(1)
print("")
print("")
time.sleep(1)
print(Fore.YELLOW+"Welcom in Saidos Tools")
print('')
print(Fore.RED+ "@SaidosHits")
time.sleep(1)
print("")
print("")
def check():
    with open("number.txt" , "r") as read:
        for lines in read:
            number = lines.rstrip("\n")
            url = "https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp"
            querystring = {"number": number,"country":"UY"}
            header ={
                "X-RapidAPI-Key": "9fb3e3de8amsh1e6649a61edaf24p1c3870jsn9cb5621555b0",
	            "X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
            }
            response = requests.request("GET",url , headers=header , params=querystring)
            data = response.json()
            valid_num = data['isValidNumber']
            isp = data['carrier']
            phone_region = data["phoneNumberRegion"]
            if True == valid_num:
              print('-'*80 +"\n" + Fore.GREEN+ number + "\n" + "ISP: "+ isp + "\n" + "Phone_ragion: " + phone_region )
            c = open('Hits.txt', 'a')
            c.writelines('-'*80 +"\n" +"Number: "+ number + '\n' + 'Carrier: '+ isp + "\n" +"Phone Region: "+ phone_region + '\n' + '-'*80 ) 
            if False == valid_num:
                print(Fore.RED +number)
        else :
            print( Fore.RED + number)

check()