
def banner():
    print("""


 ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █    ██████  ███▄    █   ▄▄███▄    ██  █▀▀ ▓█████ 
▓██   ██ ▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒ z██ ▀█   █  ▒██       ██ ▀█   █  ▒████████  ██▄█▒  ▓█   ▀ 
▓██  ▄█  ▒███   ▒▓█    ▄ ▒██░  ██▒ ▓██  ▀█ ██▒ ░ ▓██▄   ▓██  ▀█ ██▒ ▒██    ██  ▓███▄ ░ ▒███   
▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██ ▒██   ██░ ▓██▒  ▐▌██▒   ▒   ██ ▓██▒  ▐▌██▒ ░██▄▄▄▄██  ██ █▄  ▒▓█  ▄ 
░██▓ ▒██  ▒████   ▓███▀  ░ ████▓▒░ ▒██░   ▓██░ ▒██████▒ ▒██░   ▓██░  ▓█   ▓██▒ ██▒ █▄ ░▒████



                                 -ELITE-3""")
def main():
    print ("""ENTER 0 - 13 TO SELECT OPTIONS
[1] PHONE NUMBER:                 get details on a phone number
[2] IP LOOKUP:                    get details on a IP address
[3] IP PORT SCAN:                 get top port details on an IP address
[4] MAC address lookup            get details on a mac address
[5] DOMAIN LOOKUP                 get advanced details on a domain
[6] NMAP tcp scan                 get detatils of major ports in a system

[]""")
    print ("\n\n\nloading  ....")
    choice =int(input(':'))

    try:
        import phonenumbers
        import re
        import whois
        import json
        import urllib
        from haveibeenpwnd import check_email
        from haveibeenpwnd import check_password
        import requests
        from urllib.request import urlopen
    except ModuleNotFoundError:
        print("REQUIRED MODULES IS NOT INSTALLED \nPLS INSTALL REQUIREMNTS.TXT")
        choice=int(0)
    else :
        print("required modules are installed  \n skipping..... \n \n")
        print("press CTRL+C to exit \n \n")



def phonenum():
    phnum=input("ENTER PHONE NUMBER(with country code and +):  ")
    from phonenumbers import geocoder
    from phonenumbers import carrier
    from phonenumbers import timezone
    number = phonenumbers.parse(phnum)
    print("VALIDITY          :",phonenumbers.is_valid_number(number),"\n")
    print("COUNRTY           :",geocoder.description_for_number(number,'en'),"\n")
    print("CARRIER           :",carrier.name_for_number(number,'en'),"\n")
    print("TIMEZONE          :",timezone.time_zones_for_number(number),"\n")
    print("NATIONAL NO       :",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL),"\n")
    print("INTERNATIONAL NO  :",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),"\n")
    print("E164 NO           :",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164),"\n")
def iplookup():
    ip = str(input("ENTER IP :"))
    ipurl = 'http://ipinfo.io/'+ip+ '/json'
    ipresponse = urlopen(url)
    print(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    postalcode=data['postal']
    location=data['loc']
    timezone=data['timezone']

    print("IP          :",IP);print("ORG         :",org)
    print("CITY        :",city)
    print("COUNTRY     :",country)
    print("REGION      :",region)
    print("POSTAL CODE :",postalcode)
    print("LOCATION    :",location)
    print("TIMEZONE    :",timezone)
def nmap():
    nmip = str(input("ENTER IP"))
    nmres = requests.get('https://api.hackertarget.com/nmap/?q='+nmip)
    print(nmres.text)
def subnetscan():
    subip = str(input("ENTER IP RANGE \N example"))
    subres = requests.get('https://api.hackertarget.com/subnetcalc/?q='+subip)
    print(subres.text)
    
def MacAddressLookup():
    mac= str(input())
    macurl = ("https://macvendors.co/api/" + mac)
    macresponse=requests.get(macurl)
    result=macresponse.json()
    if result["result"]:
        final=result['result']
        print("Company    :" + final["company"])
        print("Address    :" + final["address"])
        print("Country    :" + final["country"])
        print("")
    else:
        print("ivaild params or mac address")

def domainlookup():
    domain=str(input("ENTER DOMAIN :"))
    domain_info = whois.whois(domain)
    for key, value in domain_info.items():
        print(key,':', value,"\n\n")
def end():
    PRINT("BYEEE")
