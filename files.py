def main():
    F1=open("gittext.txt","a")
    F1.write("Testing... 1\n 2 3\n")
    for i in range(20):
        F1.write(str(i)+"\n")
        print(F1.tell())

main()
F1=open("gittext.txt","r")
text=F1.read()
F1.close()
print(text)
""" 
path should be c:\\ or c:/
tmpfile.read(n) n characters
tmpfile.read() fullfile
tmpfile.readline() one line
tmpfile.readlines() rest of lines list of lines

os.path.isfile(logo) check if file exists

tmpfile=askopenfilename() open file dialog
 tmpfile = asksaveasfilename() save file dialog 
 
 rb read binary
 wb write binary
 a append

 dump write data in binary
input raw_input read from keyboard
 

 txt = eval(input("Enter your input: "))
print ("Received input is : ", txt)

Enter your input: [x*5 for x in range(2,10,2)] 
    Received input is : [10, 20, 30, 40]

    file object attributes: closed, mode, name

    Which Of The Following Statements Correctly Explain The Function Of Tell() Method?
 tells the current position within the file.
 indicates that the next read or write will occur at that many bytes from the beginning of the file.
 
 """