from django.shortcuts import render, redirect

def home_page(request):

    return render(request, 'base.html', {})


def encrypt_page(request):
    if request.POST.get('message') == None:
        coded = request.POST.get('message')
    else:
        coded = request.POST.get('message').lower()


    try:
        alpha_text_encrypt = {
            'a': '1',    'b': '2',      'c': '3',    'd': '4',
            'e': '5',    'f': '6',      'g': '7',    'h': '8',
            'i': '9',    'j': '$',      'k': '*',    'l': '@',
            'm': '+',    'n': '~',      'o': '-',    'p': ':',
            'q': '?',    'r': '>',      's': '!',    't': '_',
            'u': '<',    'v': ';',      'w': '|',    'x': '^',
            'y': '#',    'z': ',',      " ": '%',    "'": "^",
            ',': '/',    '1': 'a',      '2': 'z',    '3': 'f',
            '4': 'b',    '5': 'm',      '6': 'q',    '7': 'r',
            '8': 'e',    '9': 'd',      '0': 'g',
        }

        code = coded

        encrypt_message = ""
        for letter in code:
            if letter in alpha_text_encrypt.keys():
                encrypt_message += alpha_text_encrypt[letter]
            else:
                encrypt_message += ''

        result = encrypt_message

    except Exception as e:
        print("Error message is", e)


    result = encrypt_message

    context = {
        'result': result
    }

    return render(request, 'encrypt.html', context)


def decode_page(request):
    # codes = Dec.objects.last()
    if request.POST.get('message') == None:
        coded = request.POST.get('message')
    else:
        coded = request.POST.get('message').lower()


    try:
        alpha_text_decode = {
        '1': 'a',    '2': 'b',      '3': 'c',    '4': 'd',
        '5': 'e',    '6': 'f',      '7': 'g',    '8': 'h',
        '9': 'i',    '$': 'j',      '*': 'k',    '@': 'l',
        '+': 'm',    '~': 'n',      '-': 'o',    ':': 'p',
        '?': 'q',    '>': 'r',      '!': 's',    '_': 't',
        '<': 'u',    ';': 'v',      '|': 'w',    '^': 'x',
        '#': 'y',    ',': 'z',      "%": ' ',    '^': "'",
        '/': ',',    'a': '1',      'z': '2',    'f': '3',
        'b': '4',    'm': '5',      'q': '6',    'r': '7',
        'e': '8',    'd': '9',      'g': '0',
        }

        code = coded

        decoded_message = ""
        for letter in code:
            if letter in alpha_text_decode.keys():
                decoded_message += alpha_text_decode[letter]
        else:  
            decoded_message += ''

        result = decoded_message

    except Exception as e:
        print("Error message is", e)

    result = decoded_message

    context = {
        'result' : result
    }

    return render(request, 'decode.html', context)



