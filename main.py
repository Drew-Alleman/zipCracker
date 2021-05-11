import zlib
import argparse
from colorama import Fore
from zipfile import ZipFile


def crackFile(password):
    try:
        with ZipFile(args.file) as zf:
            zf.extractall(pwd=password)
            return True
    except (RuntimeError, zlib.error): # Error if password is wrong
        pass
    except NotImplementedError:
        print(error + "That compression method is not supported")
        exit()
    except IOError as e:
        print(error + str(e))
        exit()



def main():
    print(info + "Brute forcing zip file: " + args.file)
    print(info + "Using password file: " + args.wordlist)
    try:
        WordCount = len(list(open(args.wordlist, "rb")))
        print(info + "Wordcount in list: " + str(WordCount))
        if WordCount <= 1000:
            print(warning + "Wordlist contains less than 1000 words")
    except IOError as e:
        print(error + str(e))
        exit()

    crackLoop()


def crackLoop():
    count = 0
    WordCount = len(list(open(args.wordlist, "rb")))
    with open(args.wordlist, "rb") as wordListFile:
        for word in wordListFile:
            if crackFile(word.strip()):
                print("\n\n" + info + word.decode())
                exit()
            count += 1
            percent = count / WordCount
            i = int(percent * 10)
            prettyPercent = int(round(percent, 2) * 100)
            if prettyPercent < 30:
                Fore.COLOR = Fore.RED
            elif prettyPercent >= 30 and prettyPercent < 50:
                Fore.COLOR = Fore.YELLOW
            else:
                Fore.COLOR = Fore.GREEN
            b = (
                Fore.WHITE
                + "["
                + ("#" * i)
                + "." * (10 - i)
                + "] "
                + Fore.COLOR
                + "%"
                + str(prettyPercent))
            print(b, end="\r")
    print(error + 'Could not find the correct password :( ')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zip Cracker Tool")
    parser.add_argument("-w", "--wordlist", help="password list")
    parser.add_argument("-f", "--file", help="Zip file to crack", required=True)
    parser.add_argument("--white", help="Force white output", action="store_true")
    args = parser.parse_args()

    if args.white is True:
        Fore.GREEN = Fore.WHITE
        Fore.YELLOW = Fore.WHITE
        Fore.RED = Fore.WHITE

    info = Fore.GREEN + "[*] " + Fore.WHITE
    warning = Fore.YELLOW + "[!] " + Fore.WHITE
    error = Fore.RED + "[-] " + Fore.WHITE


    if args.wordlist is None:
        print(
            info
            + "No wordlist supplied using default: xato-net-10-million-passwords-10000.txt from SecLists"
        )
        args.wordlist = "xato-net-10-million-passwords-10000.txt"
    banner = (
        Fore.RED
        + f"""
  ______          ____                _             
 |__  (_)_ __    / ___|_ __ __ _  ___| | _____ _ __ 
   / /| | '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
  / /_| | |_) | | |___| | | (_| | (__|   <  __/ |   
 /____|_| .__/   \____|_|  \__,_|\___|_|\_\___|_|   
        |_|                                                                                                                   
{Fore.GREEN}[*] {Fore.WHITE}Coded by Drew Alleman
{Fore.GREEN}[*] {Fore.WHITE}Zip Cracker.\n"""
    )
    print(banner)
    main()
