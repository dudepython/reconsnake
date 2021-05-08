
def install(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install('phonenumbers')
install('re')
install('whois')
install('requests')
install('urllib')
install('json')

def banner():
    print("""


 ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █    ██████  ███▄    █   ▄▄███▄    ██  █▀▀ ▓█████ \n▓██   ██ ▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒  ██ ▀█   █  ▒██       ██ ▀█   █  ▒████████  ██▄█▒  ▓█   ▀ \n▓██  ▄█  ▒███   ▒▓█    ▄ ▒██░  ██▒ ▓██  ▀█ ██▒ ░ ▓██▄   ▓██  ▀█ ██▒ ▒██    ██  ▓███▄ ░ ▒███   \n▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██ ▒██   ██░ ▓██▒  ▐▌██▒   ▒   ██ ▓██▒  ▐▌██▒ ░██▄▄▄▄██  ██ █▄  ▒▓█  ▄ \n░██▓ ▒██  ▒████   ▓███▀  ░ ████▓▒░ ▒██░   ▓██░ ▒██████▒ ▒██░   ▓██░  ▓█   ▓██▒ ██▒ █▄ ░▒████



                                             -dudepython""")
def main():
    print ("""ENTER 0 - 13 TO SELECT OPTIONS
[1]  PHONE NUMBER:                 get details on a phone number
[2]  IP LOOKUP:                    get details on a IP address
[3]  IP PORT SCAN:                 get top port details on an IP address
[4]  MAC address lookup            get details on a mac address
[5]  DOMAIN LOOKUP                 get advanced details on a domain
[6]  SUBNET SCAN                   get detatils of major ports in a system
[7]  ASN Lookup (AS / ASN / IP)    Check an Autonomous System Number (ASN) for IP prefixes
[8]  IP GEO LOOKUP                 get lat. ,long. details of an IP
[9]  BANNER GRAB                   discover network services by simply querying the service port
[10] REVERSE DNS  
[]""")
    print ("\n\n\nloading  ....")
    
    
def load():
    import phonenumbers
    import re
    import whois
    import json
    import urllib
    import requests
    from urllib.request import urlopen
    print("required modules are installed  \n skipping..... \n \n")
    print("press CTRL+C to exit \n \n")
    run()



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
    ipresponse = urlopen(ipurl)
    print(ipurl)
    data = json.load(ipresponse)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    postalcode=data['postal']
    location=data['loc']
    timezone=data['timezone']

    print("IP          :",IP)
    print("ORG         :",org)
    print("CITY        :",city)
    print("COUNTRY     :",country)
    print("REGION      :",region)
    print("POSTAL CODE :",postalcode)
    print("LOCATION    :",location)
    print("TIMEZONE    :",timezone)
def nmap():
    import requests
    nmip = str(input("ENTER IP:  "))
    nmres = requests.get('https://api.hackertarget.com/nmap/?q='+nmip)
    print(nmres.text)
def subnetscan():
    import requests
    subip = str(input("ENTER IP RANGE:  "))
    subres = requests.get('https://api.hackertarget.com/subnetcalc/?q='+subip)
    print(subres.text)
def ansscan():
    import requests
    ansip = str(input("ENTER ASN/AS/IP:  "))
    ansres = requests.get('https://api.hackertarget.com/aslookup/?q='+ansip)
    print(ansres.text)
def geoscan():
    import requests
    geoip = str(input("ENTER IP:  "))
    geores = requests.get('https://api.hackertarget.com/geoip/?q='+geoip)
    print(geores.text)
def reversedns():
    import requests
    revip = str(input("ENTER IP:  "))
    revres = requests.get('https://api.hackertarget.com/reversedns/?q='+revip)
    print(revres.text)
def bannergrab():
    import requests
    bannerip = str(input("ENTER IP:  "))
    bannerres = requests.get('https://api.hackertarget.com/bannerlookup/?q='+bannerip)
    print(bannerres.text)
def MacAddressLookup():
    import requests
    mac= str(input("ENTER MAC ADRESS:  "))
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
    print("BYEEE see ya later ")
def start():
    load()
def run():
    banner()
    main()
    choice =int(input('ENTER CHOICE:'))
    if choice == 1:
        phonenum()
    elif choice == 2:
        iplookup()
    elif choice == 3:
        nmap()
    elif choice == 4:
        MacAddressLookup()
    elif choice == 5:
        domainlookup()
    elif choice == 6:
        subnetscan()
    elif choice == 7:
        ansscan()
    elif choice == 8:
        geoscan()
    elif choice == 9:
        bannergrab()
    elif choice ==10:
        reversedns()
print('')
start()




        
    
