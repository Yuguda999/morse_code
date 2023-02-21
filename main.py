morse_code = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.',
              'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___',
              'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___',
              'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_',
              'U': '.._', 'V': '..._', 'W': '.__', 'X': '.__', 'Y': '_.__', 'Z': '__..'}


def text_to_morse():
    '''the function converts text to morse code'''
    text = (input('Enter Text to encode: ')).upper()
    my_Morsecode = ''
    for character in text:
        if character == ' ':
            my_Morsecode += '  '
        elif character in morse_code:
            my_Morsecode += f'{morse_code[character]} '
    print(f'your encoded morse code is\n{my_Morsecode}\n')


def morse_to_text():
    '''the function converts morse code to text'''
    morse = input('Enter your morse code to decode: ')
    my_Text = ''
    for character in morse.split(' '):
        if morse[morse.split(' ').index(character):morse.split(' ').index(character) + 2] == '  ':
            my_Text += ' '
        if character in list(morse_code.values()):
            my_Text += f'{list(morse_code.keys())[list(morse_code.values()).index(character)]}'
    print(f'your decoded text is\n\t\t"{my_Text}"\n')


while True:
    print('OPTIONS:\n1. Convert text to morse code\n2. Convert morse code to text\n3. EXIT')
    choice = int(input('What would you like to do:'))
    if choice == 1:
        Text_to_morse()
    elif choice == 2:
        Morse_to_text()
    elif choice == 3:
        break
