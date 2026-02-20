def rabatt_preis(netto, rabatt_prozent):
    return netto * (1 - rabatt_prozent / 100)

def rabatt_betrag(netto, rabatt_prozent):
    return netto * rabatt_prozent / 100
