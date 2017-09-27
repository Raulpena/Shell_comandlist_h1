# Shell_comandlist_h1
First homework with a description about the shell comand list saw it in class 
Commands that we saw it in class with a little description about it

gedit(text editor) create a file with extension .csv
gedit file1.csv

cat is used for read the file
cat file1.csv

This one look for all the files.csv
for xfile in $(ls *csv)  in xfile look for all the domcuments .csv

the command echo is used to print on the terminal, the other part sed is looking for the word hello, and then change it for bye
echo "hello world!" |sed -re 's/hello/bye/;s/\s+/ /g;s/\s+//'

Like the previous one but instead of change one word, this one change blank space for underscore
echo "hello world!" | tr ' ' '_'


Changing lower to caps on the word 
echo "hello world!" | tr '[a-z]' '[A-Z]'
echo "hello world!" | tr '[:lower:]' '[:uper:]'
seq -f "Line %g" 10 | ten lines (show 10 lines) 

this one show us 3 lines of the head (the top of the text) we use 3 diferent commands to do this:
< lines head -n 3
head -n3 lines 
< lines sed -n '1,3'   it's the same, using sed
< lines awk 'NR <= 3'  the same, but with awk

in this case we look for 3 lines but now on the tail, the bottom of de text or
< lines tall -n 3 

in this one we are looking for the lines between 3 and 7 (4,5,6)
< lines awk '(NR>3)&&(NR<7)'

Looking for odd using 2 diferent commands, sed and awk
< lines sed -n '1-2p'
< awk 'NR%2' 

Like the previous one, but this one for even
< lines sed -n '0-2p'
< lines awk '(NR+1)%2'   

whith awk we are looking for the first line separeted by comma in the file  csv
awk -F',' '{print $1}' file.csv
