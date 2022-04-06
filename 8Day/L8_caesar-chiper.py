import art
import os

os.system('cls')
print(art.logo)


def do_encode(text, shift, direction):
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


      
# def do_decode(text, shift):
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     after_text = ""
#     for x in range(len(text)):
#           if text[x].lower() in alphabet:  
#             if (text[x]) in alphabet_upper:
#                     index =  (len(alphabet) - shift + alphabet.index(text[x].lower()))
#             else:
#                     index =  (alphabet.index(text[x])-shift)
#             after_text += alphabet[index]
#           else:
#             after_text += text[x]      
#     return after_text



before = "all you need is love, be happy do not worry"
shift = 10

encode = do_encode(before, shift, "encode")
print (f"The encoded text is: {encode}")
decode = do_encode(encode, shift, "decode")
print (f"The decode text is: {decode}")




