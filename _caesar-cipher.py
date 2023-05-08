import string

alphabets = list((string.ascii_lowercase + string.ascii_uppercase) * 2)
logo = '''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba,  ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    ""  ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,   ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I  88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"'  `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
print(logo)


def ceaser_cypher():
    code_route = input(
        'Do you want to encrypt or decrypt?, type in "encrypt" to encrypt or type in "decrypt" to decrypt\n').lower()

    code_route_response = ['decrypt', 'encrypt']
    while code_route not in code_route_response:
        code_route = input(
            'Please enter the right keyword❗, type in "encrypt" to encrypt or type in "decrypt" to decrypt\n')

    while True:
        try:
            shift_num = int(input('Please type in your encrypt/decrypt shift key number, it must be digits:\n'))
        except:
            print('Please make sure you only typed in an integer for your encrypt/decrypt shift number:\n')
            continue
        else:
            print('Great that is an integer\n')
            break

    shift_num %= 52

    if code_route == 'decrypt':
        shift_num *= -1

    user_text = input('Please type in or paste the text you want to encrypt or decrypt:\n')
    answer = ''

    # let's make the encryption/decryption
    for char in user_text:
        if char in alphabets:
            position = alphabets.index(char)
            end_position = position + shift_num
            answer += alphabets[end_position]
        else:
            answer += char

    print(f'\nYour {code_route}ed texts are as follows⤵:\n{answer}')


ceaser_cypher()

rerun_response = ['yes', 'no']

# let's make automate the running and quitting
rerun = True
while rerun:
    cypher_rerun = input(
        '\nHey! would you like to use this program again🙃? type "yes" to continue or "no" to discontinue\n').lower()

    while cypher_rerun not in rerun_response:
        cypher_rerun = input(
            '\nPlease use the right keyword to use this program again😐, type "yes" to continue or "no" to discontinue\n').lower()
    if cypher_rerun == 'yes':
        ceaser_cypher()
    else:
        print('Thank you for using Ceaser Cypher Encryption program by Geof..Bye now🤩.\n')
        rerun = False