#Multiple Encryption
import base64
global iterationNumber; i = 0

def decoder(decryptionInput): #This function keeps iterate the "decryptionInput" string until it solves the crypto or gives an error message if the input is not encoded in base64 format.
    tempDec2 = decryptionInput
    try:
        while True:
            tempDec = base64.b64decode(decryptionInput).decode("utf-8")
            decryptionInput = tempDec

    except Exception:
        if bool(decryptionInput == tempDec2) == True:
            print("The input message you have entered cannot be decoded. Please make sure that the message you entered is in base64 format.")

        else:
            print(decryptionInput)

def encoder(i, iterationNumber, encryptionInput): #This function encrypts "encryptionInput" string multiple times based on "iterationNumber" integer.
    while i < int(iterationNumber):
            tempEnc = base64.b64encode(encryptionInput.encode("utf-8"))
            encryptionInput = tempEnc.decode("utf-8")
            i += 1
    print(encryptionInput)

while True:
    answer = input("Please enter \"e\" for the Encryption or \"d\" for the Decryption to the command prompt:\n")
    if (answer == "e"):
        while True: # The "answer" input suppose to be a positive integer and is checking whether it meets this condition or not.
            try:
                iterationNumber = int(input("Please enter the iteration number:\n"))

            except ValueError:
                print("The entered input must be a positive integer.")
                continue

            else:
                if bool(iterationNumber > 0) == True:
                    break
                else:
                    print("The integer entered must be positive.")
                    pass

        encryptionInput = input("Enter the text that you want to encrypt:\n")
        encoder(i, iterationNumber, encryptionInput)

    elif(answer == "d"):
        decryptionInput = input("Enter the text that you want to decrypt:\n")
        decoder(decryptionInput)

    else:
        print("Incorrect input, please try again.")
