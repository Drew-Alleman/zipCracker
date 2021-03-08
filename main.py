from colorama import Fore, Style
from zipfile import ZipFile
import argparse

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
 _____       ___             _           
|_  (_)_ __ / __|_ _ __ _ __| |_____ _ _ 
 / /| | '_ \\ (__| '_/ _` / _| / / -_) '_| 
/___|_| .__/\\___|_| \\__,_\\__|_\\_\\___|_|  
       |_|                                
{Fore.GREEN}[*] {Fore.WHITE}Coded by Drew Alleman
{Fore.GREEN}[*] {Fore.WHITE}Zip Cracker.\n"""
)


def crackFile(password):
    try:
        with ZipFile(args.file) as zf:
            zf.extractall(pwd=password)
            print("\n\n" + info + password.decode())
            return True
    except IOError as e:
        print(error + str(e))
        exit()
    except:
    	return False



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
            word = word.strip()
            if crackFile(word):
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
                + str(prettyPercent)
            )
            print(b, end="\r")
    print(error + 'Could not find the correct password :( ')

print(banner)
main()
