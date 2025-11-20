def unique_in_order(sequence):
    listaFinal = []
    
    for letra in sequence:
        if not listaFinal or letra != listaFinal[-1]:
            listaFinal.append(letra)
    return listaFinal