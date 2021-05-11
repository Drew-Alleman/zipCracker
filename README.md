# Zip Cracker
Python zip cracker. 
Default password list is xato-net-10-million-passwords-10000.txt from [here](https://github.com/danielmiessler/SecLists/)

# Preview
![media](/media/preview.gif)

# Usage
```
usage: main.py [-h] [-w WORDLIST] -f FILE [--white]

Zip Cracker Tool

optional arguments:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        password list
  -f FILE, --file FILE  Zip file to crack
  --white               Force white output
```

# How to run  
```
git clone https://github.com/Drew-Alleman/zipCracker
cd zipCracker
pip install -r requirements.txt
python main.py -f <zip file to crack>
```
