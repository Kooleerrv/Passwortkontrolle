import tkinter as tk

root = tk.Tk()
class Guicreator:

    def __init__():

        self.regist = tk.Button(text="Registrieren", hight=20, width=20, command = self.Registrieren)
        self.regist.grid(row=0,column=0)

        self.login = tk.Button(text="Einloggen", hight=20, width=20, command = self.Loggin)
        self.login.grid(row=0,column=1)
        
        def Registrieren(self):


            self.VornameL = tk.Label(text="Vorname")
            self.VornameL.grid(row=1, column=0)

            self.Vorname = tk.Entry("")
            self.Vorname.grid(row=1,column=1)


            self.NachnameL = tk.Label(text="Nachname")
            self.NachnameL.grid(row=2, column=0)
            
            self.Nachname = tk.Entry("")
            self.Nachname.grid(row=2,column=1)
            

            self.EmailL = tk.Label(text="Email")
            self.EmailL.grid(row=3, column=0)
         
            self.Email = tk.Entry("")
            self.Email.grid(row=3,column=1)

            
            self.BenutzernameL = tk.Label(text="Benutzername")
            self.BenutzernameL.grid(row=4, column=0)
            
            self.Benutzername = tk.Entry("")
            self.Benutzername.grid(row=4,column=1)
            
            
            self.VornameL = tk.Label(text="Benutzername")
            self.VornameL.grid(row=5, column=0)
            
            self.Passwort = tk.Entry("")
            self.Passwort.grid(row=5,column=1)
            

            self.PasswortL = tk.Label(text="Passwort")
            self.PasswortL.grid(row=0, column=0)

            self.Passwort = tk.Entry("")
            self.Passwort.grid(row=4,column=1)

            dict = {'Vorname': VornameL, 'Nachname': NachnameL, 'Email':EmailL, 'Benutzername':BenutzernameL, 'Passwort': PasswortL}  
            
            f=open("benutzerinfoos.txt", 'a')
            print("Vorname, Nachname, Email, Benutzername, Passwort")
             
            c = f.write(dict)
            f.close()

        def Loggin(self):

            f = open("benutzerinfoos.txt", 'r')

            print("Benutzername Passwort:")
            passwortundbenutzername = input()
            def check():
                datafile = file('benutzerinfoos.txt')
                found = False
                for line in datafile:
                    if passwortundbenutzername in line:
                        found = True
                    break
                datafile.close()

            check()
            if True:
                Truelabel = tk.Label(text="True")
                TrueLabel.grid(row=0,coulmn=0)
            else:
                FalseLabel = tk.Label(text="False")
                FalseLabel.grid(row=0,coulmn=0)

                
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
                falseLabel = tk.Label(text="Wrong")
                falseLabel.grid(row=5, column=0)

      

root.mainloop()
            
        
