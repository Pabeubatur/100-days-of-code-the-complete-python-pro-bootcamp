alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
        

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text_user, shift_user):
    cipher_text = ""
    for letter in text_user:
        # with .index method we get each letter index in the alphabet and then we add the desired shift 
        posicion_lista = alphabet.index(letter) + shift_user
        # make sure index ranges from 0 - 26, if it gets 26, it starts from 0
        posicion_lista %= len(alphabet)
  
        cipher_text += alphabet[posicion_lista]

    print(cipher_text)
        
encrypt(text_user=text, shift_user=shift)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 