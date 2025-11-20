from preloaded import MORSE_CODE

def decode_morse(morseCode):
    morseCode = morseCode.strip()
    resultado = ""

    palabrasMorse = morseCode.split("   ")

    for palabra in palabrasMorse:
        letrasMorse = palabra.split(" ")
        for letra in letrasMorse:
            if letra:
                resultado += MORSE_CODE[letra]
        resultado += " "

    return resultado.strip()