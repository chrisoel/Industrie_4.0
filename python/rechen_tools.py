def netto_zu_brutto(netto, steuersatz=0.19):
    return netto * (1 + steuersatz)

def brutto_zu_netto(brutto, steuersatz=0.19):
    return brutto / (1 + steuersatz)

def ist_volljaehrig(alter):
    return alter >= 18

def differenz(a, b):
    return a - b

if __name__ == '__main__':
    print('Direkter Modulstart (Demo):')
    print('100 netto ->', netto_zu_brutto(100))
