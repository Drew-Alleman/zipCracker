from colorama import Fore, Style
from zipfile import ZipFile
from sys import stdout
import argparse
import time

info = Fore.GREEN + '[*] ' + Fore.WHITE
warning = Fore.YELLOW + '[!] ' + Fore.WHITE
error = Fore.RED + '[-] ' + Fore.WHITE

parser = argparse.ArgumentParser(description='Zip Cracker Tool')
parser.add_argument('-w', '--wordlist', metavar='-w', help='password list')
parser.add_argument('-f', '--file', metavar='f', help='Zip file to crack', required=True)
args = parser.parse_args()

if args.wordlist is None:
	print(info + 'No wordlist supplied using default: xato-net-10-million-passwords-10000.txt from SecLists')
	args.wordlist = 'xato-net-10-million-passwords.txt'
	
banner = Fore.RED + f'''
 _____       ___             _           
|_  (_)_ __ / __|_ _ __ _ __| |_____ _ _ 
 / /| | '_ \\ (__| '_/ _` / _| / / -_) '_| 
/___|_| .__/\\___|_| \\__,_\\__|_\\_\\___|_|  
       |_|                                
{Fore.GREEN}[*] {Fore.WHITE}Coded by Drew Alleman
{Fore.GREEN}[*] {Fore.WHITE}Zip Cracker.\n'''

def crackFile(password):
	try:
		with ZipFile(LockedZipFile) as zf:
			zf.extractall(pwd=password.encode())
			return True
	except KeyboardInterrupt:
		exit()
	except:
		return False


def main():
    print(info + "Brute forcing zip file: "+args.file)
    print(info + "Using password file: "+args.wordlist)
    try:
        WordCount = len(list(open(args.wordlist, "rb")))
        print(info + "Wordcount in list: " + str(WordCount))
        if WordCount <= 1000:
            print(warning + "Wordlist contains less than 1000 words")
    except IOError as e:
        print(error + str(e))
        exit(1)

    crackFile(args.wordlist,args.file)
print(banner)
main()