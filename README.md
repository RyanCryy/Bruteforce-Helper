usage for kali Linux : python3 bruteforcehelper.py input.txt output.txt

example input 
──(ryan㉿vbox)-[~/Desktop]
└─$ cat user.txt            
hello
chicken jockey
chicken lover
summer123

┌──(ryan㉿vbox)-[~/Desktop]
└─$ python3 bruteforcehelper.py user.txt result.txt 
Loaded 4 username(s) from user.txt
Generated 69 variations for: hello
Generated 138 variations for: chicken jockey
Generated 138 variations for: chicken lover
Generated 207 variations for: summer123

Total unique variations generated: 552
Results written to: result.txt

combine this with cewl for best results.
