
def Preparation(txt):
    #print(txt)
    txt=txt.lower()
    #print(txt)
    txt2=""
    for s in txt:
        #print (s)
        if s.isalnum()==True:
            txt2=txt2+s
    #print(txt2)
    return txt2

def Reverser1(txt):
    txt2=""
    for i in range(len(txt)):
        #print (i)
        #print(len(txt))
        txt2=txt2+txt[(len(txt)-1)-i]
    return txt2

def Reverser2(txt):
    txt2=""
    txt2=txt[::-1]
    return txt2

def main():
    input_txt=""
    while(True): 
        input_txt= input("Enter string to test for palindrome or 'exit': ")
        if input_txt== "exit":
            break
        #print(input_txt)
        prepared_txt=Preparation(input_txt)
        #print("Prepared txt:", prepared_txt)
        reverse_txt=Reverser2(prepared_txt)
        #print("Reverse input:", reverse_txt)
        if reverse_txt==prepared_txt:
            print("Palindrome test: True")
        else:
            print("Palindrome test: False") 
        #print(reverser_input)

if __name__ == "__main__":
    main()