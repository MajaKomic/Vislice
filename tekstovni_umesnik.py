import model

def izpis_igre(igra):
    tekst = """######################################\n
    Pravilni del gesla: {igra.pravilni_del_gesla()}\n
    Število poskusov: {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}\n
    Nepravilne črke: {igra.nepravilni_ugobi()}\n
    ##################################################\n
    """
    return tekst

def izpis_zmage(igra):
    tekst = f """#################################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
    #########################\n"""
    return tasks

def izpis_poraza(igra):
    tekst = f """#################################\n
    Porabili ste vse poskuse\n
    Pravilno geslo: {igra.geslo}\n
    #########################\n"""
    return tasks

def zahtevaj_vnos():
    return input('Vnesite črko:')

def zahtevaj_odziv_ponovni_zagon():
    return input('Za ponovni')

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.ZMAGA:
            PRINT(izpis_zmage(igra))
            break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            break
        else:
            print(izpis_igre(igra))

pozeni_vmesnik()

#testna_igra = model.nova_igra()
#print(izpis_igre(testna_igra))