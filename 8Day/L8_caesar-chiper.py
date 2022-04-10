import art
import os

os.system('cls')
print(art.logo)


def do_encode(text, shift, direction):
    while shift > 26:
        shift = shift % 26

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    after_text =""
    
    if direction == "encode":
        for x in text.lower():
            if x in alphabet:
                index = alphabet.index(x)
                if index + shift > len(alphabet)-1:
                    index = (index + shift) - (len(alphabet))
                    after_text += alphabet[index].upper()
                    #   print(alphabet[index].upper())
                else:
                    #    print(alphabet[index + shift])
                    after_text += alphabet[index + shift]
            else:
                    after_text += x
    else:
        for x in range(len(text)):
              if text[x].lower() in alphabet:  
                if (text[x]) in alphabet_upper:
                        index =  (len(alphabet) - shift + alphabet.index(text[x].lower()))
                else:
                        index =  (alphabet.index(text[x])-shift)
                after_text += alphabet[index]
              else:
                after_text += text[x]      
    return after_text  


do_continue = True
decode_text = "no"


while (do_continue):
    decode_text = input("Type 'incode' to encrypt or type 'decode' to decrypt \n")
    if (decode_text == "incode"):
        before = input("type your message for encoding: \n")
        shift = int(input("type the shift number: \n"))    
        encode = do_encode(before, shift, "encode")
        print (f"The encoded text is: {encode}")
    else:
        encode = input("type your message for decode: \n")
        shift = int(input("type the shift number: \n"))
        decode = do_encode(encode, shift, "decode")
        print (f"The decode text is: {decode}")

    result = input("are you want to continue (yes/no): \n")
    if result == "no":
        do_continue = False

print("Goodbye")



