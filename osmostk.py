from tkinter import *
from functions import calc1, calc2

fontstyle = ('Verdana', 10)
fontstyle2 = ('Verdana', 10, 'bold')
clr = '#07462a'

def calc():
    try:
        ci = float(en_ci.get())
        gv = float(en_gv.get())
        xz = float(en_xz.get())
        xp = float(en_xp.get())
        xr = float(en_xr.get())
        res_1 = calc1(ci, gv, xz, xp, xr)
        res1 = list(map(lambda x: round(x, 2), res_1))
        gi_val['text'] = res1[0]
        cv_val['text'] = res1[1]
        gp_val['text'] = res1[2]
        cp_val['text'] = res1[3]
        gk_val['text'] = res1[4]
        ck_val['text'] = res1[5]
        gr_val['text'] = res1[6]
        gs_val['text'] = res1[7]
        lp_val['text'] = res1[8]
        rp_val['text'] = res1[9]
        if en_xr2.get() != "":
            xr2 = float(en_xr2.get())
            res_2 = calc2(ci, gv, xz, xp, xr, xr2)
            res2 = list(map(lambda x: round(x, 2), res_2))
            gi_val1['text'] = res2[0]
            cv_val1['text'] = res2[1]
            gp_val1['text'] = res2[2]
            cp_val1['text'] = res2[3]
            gk_val1['text'] = res2[4]
            ck_val1['text'] = res2[5]
            gr_val1['text'] = res2[6]
            gs_val1['text'] = res2[7]
            gi_val2['text'] = res2[8]
            cv_val2['text'] = res2[9]
            gp_val2['text'] = res2[10]
            cp_val2['text'] = res2[11]
            gk_val2['text'] = res2[12]
            ck_val2['text'] = res2[13]
            gr_val2['text'] = res2[14]
            gs_val2['text'] = res2[15]
            lp_val2['text'] = res2[16]
            rp_val2['text'] = res2[17]
        warning['text'] = ""
    except ValueError:
        warning['text'] = "Fill in all entries\nwith numerical values"

root = Tk()
root.title("Reverse osmosis")
root.resizable(False, False)

# insert data
lbl_ci = Label(root, text="Ci:", font=fontstyle, fg=clr).grid(row=0, column=0)
lbl_gv = Label(root, text="Gv:", font=fontstyle, fg=clr).grid(row=1, column=0)
lbl_xz = Label(root, text="Xz:", font=fontstyle, fg=clr).grid(row=2, column=0)
lbl_xp = Label(root, text="Xp:", font=fontstyle, fg=clr).grid(row=3, column=0)
lbl_xr = Label(root, text="Xr:", font=fontstyle, fg=clr).grid(row=4, column=0)
lbl_xr2 = Label(root, text="Xr2:", font=fontstyle, fg=clr).grid(row=5, column=0)

en_ci = Entry(root, font=fontstyle)
en_ci.grid(row=0, column=1)
en_gv = Entry(root, font=fontstyle)
en_gv.grid(row=1, column=1)
en_xz = Entry(root, font=fontstyle)
en_xz.grid(row=2, column=1)
en_xp = Entry(root, font=fontstyle)
en_xp.grid(row=3, column=1)
en_xr = Entry(root, font=fontstyle)
en_xr.grid(row=4, column=1)
en_xr2 = Entry(root, font=fontstyle)
en_xr2.grid(row=5, column=1)

calcbtn = Button(root, text="Calculate", command=calc, font=fontstyle, bg=clr, fg="#fbfff0", activebackground=clr, activeforeground="#fbfff0").grid(row=6, column=0, columnspan=2, sticky="we")
warning = Label(root, text="", fg="#e60000", font=fontstyle)
warning.grid(row=7, column=0, columnspan=2, rowspan=2)

# first stage
name1 = Label(root, text="Розрахунок одноступінчатої зворотноосмотичної установки", font=fontstyle2).grid(row=0, column=2, columnspan=15)

zmish = Label(root, text="Змішувач", padx=20, font=fontstyle2).grid(row=1, column=2,columnspan=2)
lbl_gi = Label(root, text="Gi:", font=fontstyle, fg=clr).grid(row=2, column=2)
gi_val = Label(root, text="000.00", font=fontstyle)
gi_val.grid(row=2, column=3)
lbl_cv = Label(root, text="Cv:", font=fontstyle, fg=clr).grid(row=3, column=2)
cv_val = Label(root, text="000.00", font=fontstyle)
cv_val.grid(row=3, column=3)

membr = Label(root, text="Мембрана", padx=20, font=fontstyle2).grid(row=1, column=4,columnspan=2)
lbl_gp = Label(root, text="Gp:", font=fontstyle, fg=clr).grid(row=2, column=4)
gp_val = Label(root, text="000.00", font=fontstyle)
gp_val.grid(row=2, column=5)
lbl_cp = Label(root, text="Cp:", font=fontstyle, fg=clr).grid(row=3, column=4)
cp_val = Label(root, text="000.00", font=fontstyle)
cp_val.grid(row=3, column=5)
lbl_gk = Label(root, text="Gk:", font=fontstyle, fg=clr).grid(row=4, column=4)
gk_val = Label(root, text="000.00", font=fontstyle)
gk_val.grid(row=4, column=5)
lbl_ck = Label(root, text="Ck:", font=fontstyle, fg=clr).grid(row=5, column=4)
ck_val = Label(root, text="000.00", font=fontstyle)
ck_val.grid(row=5, column=5)

rozd = Label(root, text="Розділювач", padx=20, font=fontstyle2).grid(row=1, column=6,columnspan=2)
lbl_gr = Label(root, text="Gr:", font=fontstyle, fg=clr).grid(row=2, column=6)
gr_val = Label(root, text="000.00", font=fontstyle)
gr_val.grid(row=2, column=7)
lbl_cs = Label(root, text="Gs:", font=fontstyle, fg=clr).grid(row=3, column=6)
gs_val = Label(root, text="000.00", font=fontstyle)
gs_val.grid(row=3, column=7)

lp = Label(root, text="LP", font=fontstyle).grid(row=6, column=2)
lp_val = Label(root, text="000.00", font=fontstyle)
lp_val.grid(row=6, column=3)
rp = Label(root, text="RP", font=fontstyle).grid(row=6, column=4)
rp_val = Label(root, text="000.00", font=fontstyle)
rp_val.grid(row=6, column=5)

# second stage
name2 = Label(root, text="Розрахунок двоступінчатої зворотноосмотичної установки", font=fontstyle2).grid(row=7, column=2, columnspan=15)

zmish1 = Label(root, text="Змішувач", padx=20, font=fontstyle2).grid(row=8, column=2,columnspan=2)
lbl_gi1 = Label(root, text="Gi:", font=fontstyle, fg=clr).grid(row=9, column=2)
gi_val1 = Label(root, text="000.00", font=fontstyle)
gi_val1.grid(row=9, column=3)
lbl_cv1 = Label(root, text="Cv:", font=fontstyle, fg=clr).grid(row=10, column=2)
cv_val1 = Label(root, text="000.00", font=fontstyle)
cv_val1.grid(row=10, column=3)

membr1 = Label(root, text="Мембрана", padx=20, font=fontstyle2).grid(row=8, column=4,columnspan=2)
lbl_gp1 = Label(root, text="Gp:", font=fontstyle, fg=clr).grid(row=9, column=4)
gp_val1 = Label(root, text="000.00", font=fontstyle)
gp_val1.grid(row=9, column=5)
lbl_cp1 = Label(root, text="Cp:", font=fontstyle, fg=clr).grid(row=10, column=4)
cp_val1 = Label(root, text="000.00", font=fontstyle)
cp_val1.grid(row=10, column=5)
lbl_gk1 = Label(root, text="Gk:", font=fontstyle, fg=clr).grid(row=11, column=4)
gk_val1 = Label(root, text="000.00", font=fontstyle)
gk_val1.grid(row=11, column=5)
lbl_ck1 = Label(root, text="Ck:", font=fontstyle, fg=clr).grid(row=12, column=4)
ck_val1 = Label(root, text="000.00", font=fontstyle)
ck_val1.grid(row=12, column=5)

membr2 = Label(root, text="Мембрана-2", padx=20, font=fontstyle2).grid(row=8, column=6,columnspan=2)
lbl_gp2 = Label(root, text="Gp2:", font=fontstyle, fg=clr).grid(row=9, column=6)
gp_val2 = Label(root, text="000.00", font=fontstyle)
gp_val2.grid(row=9, column=7)
lbl_cp2 = Label(root, text="Cp2:", font=fontstyle, fg=clr).grid(row=10, column=6)
cp_val2 = Label(root, text="000.00", font=fontstyle)
cp_val2.grid(row=10, column=7)
lbl_gk2 = Label(root, text="Gk2:", font=fontstyle, fg=clr).grid(row=11, column=6)
gk_val2 = Label(root, text="000.00", font=fontstyle)
gk_val2.grid(row=11, column=7)
lbl_ck2 = Label(root, text="Ck2:", font=fontstyle, fg=clr).grid(row=12, column=6)
ck_val2 = Label(root, text="000.00", font=fontstyle)
ck_val2.grid(row=12, column=7)

zmish2 = Label(root, text="Змішувач-2", padx=20, font=fontstyle2).grid(row=13, column=2,columnspan=2)
lbl_gi2 = Label(root, text="Gi2:", font=fontstyle, fg=clr).grid(row=14, column=2)
gi_val2 = Label(root, text="000.00", font=fontstyle)
gi_val2.grid(row=14, column=3)
lbl_cv2 = Label(root, text="Cv2:", font=fontstyle, fg=clr).grid(row=15, column=2)
cv_val2 = Label(root, text="000.00", font=fontstyle)
cv_val2.grid(row=15, column=3)

rozd1 = Label(root, text="Розділювач", padx=20, font=fontstyle2).grid(row=13, column=4,columnspan=2)
lbl_gr1 = Label(root, text="Gr:", font=fontstyle, fg=clr).grid(row=14, column=4)
gr_val1 = Label(root, text="000.00", font=fontstyle)
gr_val1.grid(row=14, column=5)
lbl_cs1 = Label(root, text="Gs:", font=fontstyle, fg=clr).grid(row=15, column=4)
gs_val1 = Label(root, text="000.00", font=fontstyle)
gs_val1.grid(row=15, column=5)

rozd2 = Label(root, text="Розділювач-2", padx=20, font=fontstyle2).grid(row=13, column=6,columnspan=2)
lbl_gr2 = Label(root, text="Gr2:", font=fontstyle, fg=clr).grid(row=14, column=6)
gr_val2 = Label(root, text="000.00", font=fontstyle)
gr_val2.grid(row=14, column=7)
lbl_cs2 = Label(root, text="Gs2:", font=fontstyle, fg=clr).grid(row=15, column=6)
gs_val2 = Label(root, text="000.00", font=fontstyle)
gs_val2.grid(row=15, column=7)

lp2 = Label(root, text="LP", font=fontstyle).grid(row=18, column=2)
lp_val2 = Label(root, text="000.00", font=fontstyle)
lp_val2.grid(row=18, column=3)
rp2 = Label(root, text="RP", font=fontstyle).grid(row=18, column=4)
rp_val2 = Label(root, text="000.00", font=fontstyle)
rp_val2.grid(row=18, column=5)

root.mainloop()