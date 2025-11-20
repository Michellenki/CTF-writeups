-This Rick and Morty-themed challenge requires you to exploit a web server and find three ingredients to help Rick make his potion and transform himself back into a human from a pickle

-started attack machine and used opera browser to go to target IP  

-Did an nmap on target ip and saved results to a file

-view page source of shown image

-username :R1ckRul3s  

- image link  assets/rickandmorty.jpeg  

-look for robots.txt-And because search engines normally read robots.txt, Rick hides information there thinking:

“Pfft, Morty, only robots read this! No human will ever check here!”

-found "wubbalubbadubdub

-run gobuster to see if any hidden directories exist,,,use common wordlists,,include php and text files in search

-found hidden login.php and used given username and password in robots.txt

-command panel found ,ls to see folders: found 1 ingredient and clue.txt,run less for 1st answer

-command panel on webserver:create netcat listener on my server,reverse shell command can create a reverse tcp connection and connect to the box (revshells.com)

