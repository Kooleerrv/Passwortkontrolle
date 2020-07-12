

def c():

    print("Zum Registrieren: 1")
    print("Zum Einloggen: 2")

    eoderr = input()
    

    if eoderr == "1":
        f=open("benutzerinfoos.txt", 'a')

        print("Vorname, Nachname, Email, Benutzername, Passwort")
        benutzerinfos = str(input()+"\n")
        c = f.write(benutzerinfos)
        f.close()
    elif eoderr == "2":

        f = open("benutzerinfoos.txt", 'r')

        print("Benutzername Passwort:")
        passwortundbenutzername = input()

        
        vnnnembnpw = f.read()
        vnnnembnpw = vnnnembnpw.replace(",", "")
        vnnnembnpw = vnnnembnpw.split()
        vnnnembnpw = vnnnembnpw[:-3]
        vnnnembnpw = str(vnnnembnpw)
        vnnnembnpw = vnnnembnpw.replace("[", "")
        vnnnembnpw = vnnnembnpw.replace("]", "")
        vnnnembnpw = vnnnembnpw.replace("'", "")

        

        if vnnnembnpw == passwortundbenutzername:
            print ("True")

        elif vnnnembnpw != passwortundbenutzername:
            print ("False")

    
c()
