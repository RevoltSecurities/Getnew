# Getnew
Getnew a python based tool find unique and new lines and words or even for subdomains

# Features
- Supports stdin/stdout
- Removes and get only unique lines
- Can give n number of file to campare with another file and get unique things

# Installation:

```bash
git clone https://github.com/sanjai-AK47/Getnew.git
pip install .
getnew -h
```

# Usage:

```bash
getnew -h                                                                    
usage: getnew [-h] -c COMPARE [-f [FILENAME ...]] [-o OUTPUT] [-s]

Get new is a tool to get unique subdomains and skip duplicated

options:
  -h, --help            show this help message and exit
  -c COMPARE, --compare COMPARE
                        [INFO]: File to compare with n number of files
  -f [FILENAME ...], --filename [FILENAME ...]
                        [INFO]: Files to compare and get unique ones
  -o OUTPUT, --output OUTPUT
                        [INFO]: Filename to save the unique ones
  -s, --silent          [INFO]: Banner and version will not be printed in console to user

```

# Workflows:

```bash
cat old_data.txt
www.apple.com
api.apple.com
prod.apple.com
```

```bash
cat new_data.txt
www.apple.com
api.apple.com
prod.apple.com
new.apple.com
new.api.apple.com
newton.apple.com
```

```bash
cat old_data.txt | getnew -c new_data.txt -o results.txt --silent
new.apple.com
new.api.apple.com
newton.apple.com
```

This how the workflow of the getnew to shows how it works

## Information :

Getnew is different than anew of [tomnomnom](https://github.com/tomnomnom/anew) and it workflow so you can not confuse the working of these tool
you can compare the both workflow of tomnomnom's anew and getnew :)
