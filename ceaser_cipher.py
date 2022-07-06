def encrypt(a,key):
    i = 0
    
    while(i<len(a)):
        a[i] = a[i] + key
        i=i+1
    return "".join(a)

def main():
    a = input("Enter your message  :  ")
    lis =list(a)
    key = input("Enter encryption text :  ")
    encrypted_text = encrypt(lis,key)
    print("Encrypted text is ",encrypted_text)
if __name__ == "__main__":
    main()
