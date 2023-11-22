import random 
from colorama import Fore, Style
import argparse
import sys 
import os

red = Fore.RED
green = Fore.GREEN
magenta = Fore.MAGENTA
cyan = Fore.CYAN
mixed = Fore.RED + Fore.BLUE
blue = Fore.BLUE
yellow = Fore.YELLOW
white = Fore.WHITE
reset = Style.RESET_ALL
bold = Style.BRIGHT
colors = [green, cyan, blue]
random_color = random.choice(colors)



banner = f"""{bold}{random_color} 
   ______     __  _   __            
  / ____/__  / /_/ | / /__ _      __
 / / __/ _ \/ __/  |/ / _ \ | /| / /
/ /_/ /  __/ /_/ /|  /  __/ |/ |/ / 
\____/\___/\__/_/ |_/\___/|__/|__/  
                                  
                                  
                          {bold}{white}Author: D.Sanjai Kumar @CyberRecoltSecurities {reset}        
                                    {reset}"""

parser = argparse.ArgumentParser(description=f"{bold}{white}Get new is a tool to get unique subdomains and skip duplicated")

parser.add_argument("-c", "--compare", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}File to compare with n number of files", type=str, required=True)

parser.add_argument("-f", "--filename", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Files to compare and get unique ones", nargs="*")

parser.add_argument("-o", "--output", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Filename to save the unique ones", type=str)

parser.add_argument("-s", "--silent", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Banner and version will not be printed in console to user ", action="store_true")


args = parser.parse_args()




def get_version():
    
    version = "v1.0.0"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Getnew/releases/latest"
    
    try:
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                message = "latest"
                
                print(f"[{bold}{blue}Version{reset}]: {bold}{white}Getnew current version {version} ({green}{message}{reset})")
                
                t.sleep(1)
                
            else:
                
                message ="outdated"
                
                print(f"[{bold}{blue}Version{reset}]: {bold}{white}Getnew current version {version} ({red}{message}{reset})")
                
                t.sleep(1)
                
        else:
            
            pass
        
    except KeyboardInterrupt as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Getnew says BYE!")
        
        exit()
        
                
    except Exception as e:
        
        pass


def unique_flags(files, cfiles):
    
    for file in files:
        
        with open(file, "r") as domains:
            
            subdomains = set(domains.read().splitlines())
            
            
    with open(cfiles, "r") as domains:
            
            subdomains_one = set(domains.read().splitlines())
      
    all_uniques = subdomains_one - subdomains

    for subdomain in all_uniques:
        
        print(subdomain)
        
        save(subdomain)
        
def unique_stdin(subdomains, cfile) :
    
    with open(cfile, "r") as domains:
            
        subdomains_one = set(domains.read().splitlines())
        
    all_uniques = subdomains_one - subdomains

    for subdomain in all_uniques:
        
        print(subdomain)
        
        save(subdomain)
    
    
    
    

def save(subdomain):
    
    try:
        
        if args.output:
            
            if os.path.isfile(args.output):
                
                filename = args.output
                
            elif os.path.isdir(args.output):
                
                filename = os.path.join(args.output, "getnew_results.txt")
                
            else:
                
                filename = args.output
                
                
        if not args.output:
            
            filename = "getnew_results.txt"
        
        with open(filename, "a") as w:
            
            w.write(subdomain + '\n')
            
    except KeyboardInterrupt as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Getnew says BYE!")
        
        exit()
        
    except Exception as e:
        
        pass   

def main():
    
    try:
        
        if args.filename and args.compare:
            
            if not args.silent:
                
                print(banner)
                
                get_version()
            
            unique_flags(args.filename, args.compare)
        
        else:
            
            if not args.silent:
                
                print(banner)
                
                get_version()
            
            subdomains = {subdomain.strip() for subdomain in sys.stdin}
            
            unique_stdin(subdomains, args.compare)
                
    except KeyboardInterrupt as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Getnew says BYE!{reset}")
        
        exit()
        
    except Exception as e:
        
        pass 

if __name__ == '__main__':
    
    main()
