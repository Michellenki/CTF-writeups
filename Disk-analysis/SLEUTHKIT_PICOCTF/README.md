SLEUTHKIT APPRENTICE

Used wget to download the compressed disk image in tmp directory

Used gunzip to uzip since its a .gz

Sleuthkit tool mmls to show the partition table

Noticed the main partition: largest with uneven length( the sure way is to check the one labelled 'Linux (0x83) '

fls requires arguments eg,,-o imgoffset: Offset into image file (in sectors)
  
IF inode is not specified ,,root dir is used

Use fls -o mainpartitionstartvalue flename to see major directories in main partition

Next repeat the command above but include either root or home dir inode

Found 2 files in root directory {one was reallocatted after deletion)

The other file contained the flag,,,used sleuthkit icat -o startvalue filename inode

solved!
