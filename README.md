# Find-py

### Description

* A "**find**" tool purely written in **Python**, like "find" in Linux
* Support customized filter **plugins**
* **Why** write this tool
  * for practice
  * a small tool that I can use to find a certain file or folder with customized filter plugins 

### Usage

```
python find-py.py -p ~/Documents -n file-to-find.txt -t file -s gt20
```

* **-p** :  path where to begin search, default is **current folder**
* **-n** :  target file name or regex (if want to use regex, **-r** should be used)
* **-t**  :  type of target, can be *file*, *folder*, *all*
* **-s**  :  size of file (only for **file** but not folder), **gt** means "greater than", **gt20** means "greater than 20 bytes"
* **-h**  :  know more arguments here
* Futhermore, users can write customized plugin to filter file