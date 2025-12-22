LAYERS OF DISK IMAGES

 Media - mmls tool that gives partition table

 Block - blkcat outputs the context of a single block
 
 Inode - icat outputs single file based on inode no
 
 Filename - fls lists files on image from root

 This one was a little tough encryption was introduced

 So I unziped,,used mmls for partition table,,,used fls and found them in the root folder

 it contained ash_history and and encrypted plus deleted version of the filr

 ashhistory had the password used,

 Extracted encrypted data using  cat offset from disk image (+ encrypted file inode) and directed output to the encrypted file this output confirms AES encryption,password based and OpenSSL
 
 I then used file <filename>  to identify file type

 decrypted using -d ,the salt value ,encrypted file as in and sent output to the unencrypted version of the image(-out) -k <password>
