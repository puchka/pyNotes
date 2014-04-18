#/usr/bin/env python
# -*- coding:Latin-1 -*-

from Tkinter import *

class Notes(Frame):
    def __init__(self):
        Frame.__init__(self,bg="#0099FF")
        self.master.title('Notes')
        self.grid()
        
        # Barèmes
        
        bareme = Frame(self,bg="#0099FF")
        bareme.grid(row=1)
        Label(bareme,text='Barèmes : ',
              font=("Times New Roman","16"),
              bg="#0099FF").grid(row=1,
                                 column=1)
        seriC = Button(bareme,text='Série C',
                       font=("Comic Sans MS","12"),
                       bg="#CC0033",
                       command=self.serieC)
        seriC.grid(row=1,column=2,padx=2,pady=3)
        seriD = Button(bareme,text='Série D',
                       font=("Comic Sans MS","12"),
                       bg="#CCCCFF",
                       command=self.serieD)
        seriD.grid(row=1,column=3,padx=2,pady=3)

        # Matières scientifiques

        matSc = Frame(self,bd=2,relief=SUNKEN,
                      bg="#33CCFF")
        matSc.grid(row=2,padx=5,pady=5)
        Label(matSc,text='Matières scientifiques',
              font=("Papyrus","16"),
              bg="#33CCFF").grid(row=1,
                                 column=1,
                                 columnspan=4)
        # Maths
        Label(matSc,text='Mathématiques : ',
              bg="#33CCFF").grid(row=2,column=1)
        self.maths = Entry(matSc)
        self.maths.grid(row=2,column=2,padx=3)
        Label(matSc,text='Coefficient : ',
              bg="#33CCFF").grid(row=2,column=3)
        self.varCmat = IntVar()
        self.varCmat.set("1")
        self.coefMat = Entry(matSc,textvariable=self.varCmat)
        self.coefMat.grid(row=2,column=4,padx=3)
        # P.C.
        Label(matSc,text='P.C. : ',
              bg="#33CCFF").grid(row=3,column=1)
        self.pc = Entry(matSc)
        self.pc.grid(row=3,column=2)
        Label(matSc,text='Coefficient : ',
              bg="#33CCFF").grid(row=3,column=3)
        self.varCpc = IntVar()
        self.varCpc.set("1")
        self.coefPc = Entry(matSc,textvariable=self.varCpc)
        self.coefPc.grid(row=3,column=4)
        # S.V.T.
        Label(matSc,text='S.V.T. : ',
              bg="#33CCFF").grid(row=4,column=1)
        self.svt = Entry(matSc)
        self.svt.grid(row=4,column=2)
        Label(matSc,text='Coefficient : ',
              bg="#33CCFF").grid(row=4,column=3)
        self.varCsvt = IntVar()
        self.varCsvt.set("1")
        self.coefSvt = Entry(matSc,textvariable=self.varCsvt)
        self.coefSvt.grid(row=4,column=4)
        # Moyenne scientifique
        Label(matSc,
              text='Moyenne scientifique : ',
              bg="#33CCFF").grid(row=5,column=1,
                                 columnspan=2,pady=10)
        self.varMoySc = IntVar()
        moySc = Entry(matSc,textvariable=self.varMoySc)
        moySc.grid(row=5,column=3,columnspan=2,pady=10)

        # Matières littéraires

        matLit = Frame(self,bd=2,relief=SUNKEN,
                       bg="#FF9999")
        matLit.grid(row=3)
        Label(matLit,text='Matières littéraires',
              font=("Amaze","20"),
              bg="#FF9999").grid(row=1,column=1,
                                 columnspan=4)
        # Français
        Label(matLit,text='Français : ',
              bg="#FF9999").grid(row=2,column=1)
        self.fr = Entry(matLit)
        self.fr.grid(row=2,column=2,padx=3)
        Label(matLit,text='Coefficient : ',
              bg="#FF9999").grid(row=2,column=3)
        self.varCfr = IntVar()
        self.varCfr.set("1")
        self.coefFr = Entry(matLit,textvariable=self.varCfr)
        self.coefFr.grid(row=2,column=4,padx=3)
        # Anglais
        Label(matLit,text='Anglais : ',
              bg="#FF9999").grid(row=3,column=1)
        self.ang = Entry(matLit)
        self.ang.grid(row=3,column=2)
        Label(matLit,text='Coefficient : ',
              bg="#FF9999").grid(row=3,column=3)
        self.varCang = IntVar()
        self.varCang.set("1")
        self.coefAng = Entry(matLit,textvariable=self.varCang)
        self.coefAng.grid(row=3,column=4)
        # Malagasy
        Label(matLit,text='Malagasy : ',
              bg="#FF9999").grid(row=4,column=1)
        self.mal = Entry(matLit)
        self.mal.grid(row=4,column=2)
        Label(matLit,text='Coefficient : ',
              bg="#FF9999").grid(row=4,column=3)
        self.varCmal = IntVar()
        self.varCmal.set("1")
        self.coefMal = Entry(matLit,textvariable=self.varCmal)
        self.coefMal.grid(row=4,column=4)
        # Philosophie
        Label(matLit,text='Philosophie : ',
              bg="#FF9999").grid(row=5,column=1)
        self.philo = Entry(matLit)
        self.philo.grid(row=5,column=2)
        Label(matLit,text='Coefficient : ',
              bg="#FF9999").grid(row=5,column=3)
        self.varCphilo = IntVar()
        self.varCphilo.set("1")
        self.coefPhilo = Entry(matLit,textvariable=self.varCphilo)
        self.coefPhilo.grid(row=5,column=4)
        # H.G.
        Label(matLit,text='H.G. : ',
              bg="#FF9999").grid(row=6,column=1)
        self.hg = Entry(matLit)
        self.hg.grid(row=6,column=2)
        Label(matLit,text='Coefficient : ',
              bg="#FF9999").grid(row=6,column=3)
        self.varChg = IntVar()
        self.varChg.set("1")
        self.coefHg = Entry(matLit,textvariable=self.varChg)
        self.coefHg.grid(row=6,column=4)
        # Moyenne littéraire
        Label(matLit,
              text='Moyenne littéraire :',
              bg="#FF9999").grid(row=7,column=1,
                                 columnspan=2,pady=10)
        self.varMoyLit = IntVar()
        self.moyLit = Entry(matLit,textvariable=self.varMoyLit)
        self.moyLit.grid(row=7,column=3,columnspan=2,pady=10)

        # E.P.S.

        eps = Frame(self,bd=2,relief=GROOVE,bg="#669999")
        eps.grid(row=4,pady=5)
        Label(eps,text='E.P.S. : ',
              bg="#669999").grid(row=1,column=1,pady=3)
        self.eps = Entry(eps)
        self.eps.grid(row=1,column=2,padx=3)
        Label(eps,text='Coefficient : ',
              bg="#669999").grid(row=1,column=3,pady=3)
        self.varCeps = IntVar()
        self.varCeps.set("1")
        self.coefEps = Entry(eps,textvariable=self.varCeps)
        self.coefEps.grid(row=1,column=4,padx=3)

        # Observations

        obs = Frame(self,bd=2,relief=RAISED,bg="#CC6633")
        obs.grid(row=5,pady=3)
        Label(obs,text='Moyenne générale : ',
              bg="#CC6633").grid(row=1,column=1,pady=3)
        self.varMoyG = IntVar()
        self.moyGen = Entry(obs,textvariable=self.varMoyG)
        self.moyGen.grid(row=1,column=2,padx=3,pady=3)

        Label(obs,text='Mention : ',
              bg="#CC6633").grid(row=2,column=1,pady=3)
        self.varMen = StringVar()
        self.men = Entry(obs,textvariable=self.varMen)
        self.men.grid(row=2,column=2,padx=3,pady=3)

        # Mise en marche

        Button(self,text='GO',font=("Viner Hand ITC","16"),
               command=self.go,bg="#0000CC",
               width=7,height=1).grid(row=6,
                                      pady=5)

        self.master.update()
        self.master.geometry(self.master.geometry())
        

    def serieC(self):
        "barème série C"
        self.varCmat.set("5")
        self.varCpc.set("5")
        self.varCsvt.set("2")
        self.varCfr.set("2")
        self.varCang.set("Bonus")
        self.varCmal.set("3")
        self.varCphilo.set("2")
        self.varChg.set("2")
        self.varCeps.set("1")

    def serieD(self):
        "barème série D"
        self.varCmat.set("4")
        self.varCpc.set("4")
        self.varCsvt.set("4")
        self.varCfr.set("2")
        self.varCang.set("Bonus")
        self.varCmal.set("3")
        self.varCphilo.set("2")
        self.varChg.set("2")
        self.varCeps.set("1")

    def go(self):
        "mise en marche"
        try:
            mat1=float(self.maths.get())
        except:
            mat1=0
        coefMat=float(self.coefMat.get())
        mat = mat1*coefMat
        
        try:
            pc1=float(self.pc.get())
        except:
            pc1=0
        coefPc=float(self.coefPc.get())
        pc = pc1*coefPc
        
        try:
            svt1=float(self.svt.get())
        except:
            svt1=0
        coefSvt=float(self.coefSvt.get())
        svt=svt1*coefSvt

        tSc=mat+pc+svt
        cSc=coefMat+coefPc+coefSvt
        moySc=tSc/cSc
        self.varMoySc.set(str(moySc))

        try:
            fr1=float(self.fr.get())
        except:
            fr1=0
        coefFr=float(self.coefFr.get())
        fr=fr1*coefFr

        try:
            ang1=float(self.ang.get())
        except:
            ang1=0
        ang_=self.coefAng.get()
        if ang_ in ("b","B","bonus","Bonus"):
            if ang1 > 10:
                ang=ang1-10
            else:
                ang=0
        else:
            coefAng=float(self.coefAng.get())
            ang=ang1*coefAng

        try:
            mal1=float(self.mal.get())
        except:
            mal1=0
        coefMal=float(self.coefMal.get())
        mal=mal1*coefMal

        try:
            philo1=float(self.philo.get())
        except:
            philo1=0
        coefPhilo=float(self.coefPhilo.get())
        philo=philo1*coefPhilo

        try:
            hg1=float(self.hg.get())
        except:
            hg1=0
        coefHg=float(self.coefHg.get())
        hg=hg1*coefHg

        if ang_ in ("b","B","bonus","Bonus"):
            tLit=fr+mal+philo+hg
            cLit=coefFr+coefMal+coefPhilo+coefHg
        else:
            tLit=fr+ang+mal+philo+hg
            cLit=coefFr+coefAng+coefMal+coefPhilo+coefHg
        moyLit=tLit/cLit
        self.varMoyLit.set(str(moyLit))

        try:
            eps1=float(self.eps.get())
        except:
            eps1=0
        coefEps=float(self.coefEps.get())
        eps=eps1*coefEps

        if ang_ in ("b","B","bonus","Bonus"):
            tG=tSc+tLit+ang+eps
            cG=cSc+cLit+coefEps
        else:
            tG=tSc+tLit+ang+eps
            cG=cSc+cLit+coefAng+coefEps
        moyG=tG/cG
        self.varMoyG.set(float(moyG))

        if moyG < 9.5:
            mention="Tsy afaka!"
        elif 9.5<=moyG<12:
            mention="Passable"
        elif 12<=moyG<14:
            mention="Assez Bien"
        elif 14<=moyG<16:
            mention="Bien"
        else:
            mention="Très Bien"
        self.varMen.set(mention)


Notes().mainloop()
