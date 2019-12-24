#!/bin/python3
try :
    import multiprocessing
    import time
    import os
    import colorama
    import requests
    import urllib.parse
    import urllib.error
    import ssl
    import sys
    import threading
    import itertools
    from pytube import YouTube
    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen

    # I HAVE NO FUCKIN IDEA
        # LETS CLEAR FOR A MORE WHOLESOME UX
    os.system("clear")

        # MAKE A LOGO
    def logo():
        print("\n")
        print("\x1b[1;34m" + "        ██████╗ " + "\x1b[0m","\x1b[1;33m" + "██╗   ██╗  " + "\x1b[0m","\x1b[1;91m" + "██╗      ██████╗  █████╗ ██████╗ " + "\x1b[0m")
        print("\x1b[1;34m" + "        ██╔══██╗" + "\x1b[0m","\x1b[1;33m" + "╚██╗ ██╔╝  " + "\x1b[0m","\x1b[1;91m" + "██║     ██╔═══██╗██╔══██╗██╔══██╗" + "\x1b[0m")
        print("\x1b[1;34m" + "        ██████╔╝" + "\x1b[0m","\x1b[1;33m" + " ╚████╔╝   " + "\x1b[0m","\x1b[1;91m" + "██║     ██║   ██║███████║██║  ██║" + "\x1b[0m")
        print("\x1b[1;34m" + "        ██╔═══╝ " + "\x1b[0m","\x1b[1;33m" + "  ╚██╔╝    " + "\x1b[0m","\x1b[1;91m" + "██║     ██║   ██║██╔══██║██║  ██║" + "\x1b[0m")
        print("\x1b[1;34m" + "        ██║     " + "\x1b[0m","\x1b[1;33m" + "   ██║     " + "\x1b[0m","\x1b[1;91m" + "███████╗╚██████╔╝██║  ██║██████╔╝" + "\x1b[0m")
        print("\x1b[1;34m" + "        ╚═╝     " + "\x1b[0m","\x1b[1;33m" + "   ╚═╝     " + "\x1b[0m","\x1b[1;91m" + "╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ " + "\x1b[0m")
        print("\n\t\x1b[96;1m" + "BY @spooky_sec : " + "\x1b[0m", "\x1b[38;5;92;4m" + "https://instagram.com/spooky_sec" + "\x1b[0m" )
        print("\n\t\x1b[97;1m" + "note : video quality will depend on your internet speed." + "\x1b[0m")
        print("\n\t\x1b[97;1m" + "note : some videos CANNOT be downloaded due to how YouTube works." + "\x1b[0m")
    logo()


        # TO IGNORE SOME SSL SHIT
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE




        # TAKE THE URL
    try :
        url  = input("\n\t[+] PLEASE ENTER A URL   :   ")
        print()
    except KeyboardInterrupt :
        os.system("clear")
        print("\tBYE BITCH")
        sys.exit(1)


        # DEFINE SOME SHIT
    try :
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # MAKING SURE YOU ARE'NT A BOT! btw YOU ARE |:
    except ValueError :
        time.sleep(2)
        print("\t[!] VIDEO DOES NOT EXIST!")
        input("\n\t[+] PRESS ENTER TO EXIT ")
        sys.exit(0)

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    video_details = {}

        # GET THE VIDEO TITLE
    for span in soup.findAll('span',attrs={'class': 'watch-title'}):
        shhiiit = video_details['TITLE'] = span.text.strip()
        data = "'" + shhiiit + "'"
        print("\t[*] VIDEO TITLE  :  " + data + "\n")

        # USELESS FANCY LOADING
    animation = False

    def animate():
        for shit in itertools.cycle(['|', '/', '-', '\\']):
            if animation:
                break
            sys.stdout.write("\r\t[*] DOWNLOADING VIDEO! " + shit)
            sys.stdout.flush()
            time.sleep(0.1)
    t = threading.Thread(target=animate)
    t.start()
    try :
        YouTube(url).streams.first().download()
        animation = True
    except KeyError:
        animation = True
        os.system("clear")
        print("\n\t[!] COULDN'T DOWNLOAD VIDEO, SORRY!\n\n")
        exit(0)

    print()
    print("\n\t[!] SAVED ( " + data + " )")
    print("\n\t[!] DONE!")
    print("\n\t[!] CLEARING ...")
    time.sleep(3)
    os.system("clear")
    sys.exit(0)
except KeyboardInterrupt:
    os.system("clear")
    sys.exit(1)
        # TESTING YOUTUBE VIDEO  https://www.youtube.com/watch?v=iDO9J_3OVJ0

      # CLEARING IS FOR GODS
