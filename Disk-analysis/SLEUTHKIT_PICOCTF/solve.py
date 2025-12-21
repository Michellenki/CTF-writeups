import os

1: Unzip the file

os.system("gunzip -k disk.flag.img.gz")


2: List the files in the 3rd partition (The offset 360448 is the 'address' of that section)

We use 'fls' to look and 'grep' to search for the word 'flag'
os.system("fls -o 360448 -r disk.flag.img | grep flag")

3: Once you see the number (inode) next to flag.txt, you use 'icat' to read it

