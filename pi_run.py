from random import random
from statistics import mean
from statistics import stdev
import numpy as np
import tkinter as tk
from tkinter import *
from pi_roll import min_expect, max_expect, shots_blast, hitting, wounding, save, save2, mw_number, damage_mw, damage, damage2

##hover wiget
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
##re-rolling once reader
def rr_one():
	dict_1 = {}
	if btn_hit["text"] == "reroll once":
		dict_1['rh'] = 1
	elif btn_hit["text"] == "reroll twice":
		dict_1['rh'] = 2
	elif btn_hit["text"] == "reroll thrice":
		dict_1['rh'] = 3
	else:
		dict_1['rh'] = 0
		
	if btn_wnd_rr["text"] == "reroll once":
		dict_1['rw'] = 1
	elif btn_wnd_rr["text"] == "reroll twice":
		dict_1['rw'] = 2
	elif btn_wnd_rr["text"] == "reroll thrice":
		dict_1['rw'] = 3
	else:
		dict_1['rw'] = 0
		
	if btn_sv_rr["text"] == "reroll once":
		dict_1['rs'] = 1
	elif btn_sv_rr["text"] == "reroll twice":
		dict_1['rs'] = 2
	elif btn_sv_rr["text"] == "reroll thrice":
		dict_1['rs'] = 3
	else:
		dict_1['rs'] = 0
	return dict_1
##wiget commands
def incr_bs():
	value = int(bs_int["text"])
	if value < 6:
		bs_int["text"] = f"{value + 1}"
def decr_bs():
	value = int(bs_int["text"])
	if value > 2:
		bs_int["text"] = f"{value - 1}"
def incr_w():
	value = int(w_int["text"])
	if value < 6:
		w_int["text"] = f"{value + 1}"
def decr_w():
	value = int(w_int["text"])
	if value > 2:
		w_int["text"] = f"{value - 1}"
def incr_sv():
	value = int(sv_int["text"])
	if value < 7:
		sv_int["text"] = f"{value + 1}"
def decr_sv():
	value = int(sv_int["text"])
	if value > 2:
		sv_int["text"] = f"{value - 1}"
def incr_d_int():
	value = int(d_int["text"])
	if value < 12 and btn_d_int["text"] == "d int on":
		d_int["text"] = f"{value + 1}"
def decr_d_int():
	value = int(d_int["text"])
	if value > 1 and btn_d_int["text"] == "d int on":
		d_int["text"] = f"{value - 1}"
def incr_d_add():
	value = int(d_add_int["text"])
	if value < 10:
		d_add_int["text"] = f"{value + 1}"
def decr_d_add():
	value = int(d_add_int["text"])
	if value > -1:
		d_add_int["text"] = f"{value - 1}"
def incr_d_min():
	value = int(min_d_int["text"])
	if value < 3 and btn_d_int["text"] == 'd int off':
		min_d_int["text"] = f"{value + 1}"
def decr_d_min():
	value = int(min_d_int["text"])
	if value > 1 and btn_d_int["text"] == 'd int off':
		min_d_int["text"] = f"{value - 1}"
def fct_hit_rr():
	if btn_hit["text"] == 'reroll off':
		btn_hit["text"] = "reroll once"
	elif btn_hit["text"] == "reroll once":
		btn_hit["text"] = "reroll twice"
	elif btn_hit["text"] == "reroll twice":
		btn_hit["text"] = "reroll thrice"
	elif btn_hit["text"] == "reroll thrice":
		btn_hit["text"] = "reroll 1s"
	elif btn_hit["text"] == 'reroll 1s':
		btn_hit["text"] = "reroll all"
	else:
		btn_hit["text"] = "reroll off"
def def_h_rr():
	if btn_hit["text"] == "reroll once":
		return "reroll off"
	elif btn_hit["text"] == "reroll twice":
		return "reroll off"
	elif btn_hit["text"] == "reroll thrice":
		return "reroll off"
	else:
		return btn_hit["text"]
def fct_hit_exp():
	if btn_exp["text"] == 'explode off':
		btn_exp["text"] = "6s explode 2"
		btn_dka["text"] = "dakka off"
		btn_flm["text"] = "flame off"
		btn_blst["text"] = "blast off"
	elif btn_exp["text"] == '6s explode 2':
		btn_exp["text"] = "6s explode 3"
	elif btn_exp["text"] == '6s explode 3':
		btn_exp["text"] = "6s explode 4"

	elif btn_exp["text"] == '6s explode 4':
		btn_exp["text"] = "5s explode 2"
	elif btn_exp["text"] == '5s explode 2':
		btn_exp["text"] = "5s explode 3"
	elif btn_exp["text"] == '5s explode 3':
		btn_exp["text"] = "5s explode 4"

	elif btn_exp["text"] == '5s explode 4':
		btn_exp["text"] = "4s explode 2"
	elif btn_exp["text"] == '4s explode 2':
		btn_exp["text"] = "4s explode 3"
	elif btn_exp["text"] == '4s explode 3':
		btn_exp["text"] = "4s explode 4"

	else:
		btn_exp["text"] = "explode off"
def fct_hit_dakka():
	if btn_dka["text"] == 'dakka off':
		btn_dka["text"] = "dakka on"
		btn_flm["text"] = "flame off"
		btn_blst["text"] = "blast off"
		btn_exp["text"] = "explode off"
	else:
		btn_dka["text"] = "dakka off"
def fct_hit_flm():
	if btn_flm["text"] == 'flame off':
		btn_flm["text"] = "flame D3"
		btn_blst["text"] = "blast off"
		btn_exp["text"] = "explode off"
		btn_dka["text"] = "dakka off"
		btn_hit["text"] = "reroll off"
		btn_h6iw["text"] = "6 wound off"
	elif btn_flm["text"] == 'flame D3':
		btn_flm["text"] = "flame D6"
	elif btn_flm["text"] == 'flame D6':
		btn_flm["text"] = "flame D6+2"
	elif btn_flm["text"] == 'flame D6+2':
		btn_flm["text"] = "flame 2D6"
	else:
		btn_flm["text"] = "flame off"
def fct_hit_blst():
	if btn_blst["text"] == 'blast off':
		btn_blst["text"] = "blast D3"
		btn_dka["text"] = "dakka off"
		btn_flm["text"] = "flame off"
		btn_exp["text"] = "explode off"
	elif btn_blst["text"] == 'blast D3':
		btn_blst["text"] = "D3"
	elif btn_blst["text"] == 'D3':
		btn_blst["text"] = "blast D6"
	elif btn_blst["text"] == 'blast D6':
		btn_blst["text"] = "D6"
	elif btn_blst["text"] == 'D6':
		btn_blst["text"] = "blast 2D3"
	elif btn_blst["text"] == 'blast 2D3':
		btn_blst["text"] = "2D3"
	elif btn_blst["text"] == '2D3':
		btn_blst["text"] = "blast 3D3"
	elif btn_blst["text"] == 'blast 3D3':
		btn_blst["text"] = "3D3"
	elif btn_blst["text"] == '3D3':
		btn_blst["text"] = "blast 2D6"
	elif btn_blst["text"] == 'blast 2D6':
		btn_blst["text"] = "2D6"
	elif btn_blst["text"] == '2D6':
		btn_blst["text"] = "blast 4D6"
	elif btn_blst["text"] == 'blast 4D6':
		btn_blst["text"] = "4D6"
	else:
		btn_blst["text"] = "blast off"
def fct_hit_h6iw():
	if btn_h6iw["text"] == '6 wound off':
		btn_h6iw["text"] = "6 wound on"
		btn_flm["text"] = "flame off"
	else:
		btn_h6iw["text"] = "6 wound off"
def fct_w_rr():
	if btn_wnd_rr["text"] == 'reroll off':
		btn_wnd_rr["text"] = "reroll once"
	elif btn_wnd_rr["text"] == "reroll once":
		btn_wnd_rr["text"] = "reroll twice"
	elif btn_wnd_rr["text"] == "reroll twice":
		btn_wnd_rr["text"] = "reroll thrice"
	elif btn_wnd_rr["text"] == "reroll thrice":
		btn_wnd_rr["text"] = "reroll 1s"
	elif btn_wnd_rr["text"] == 'reroll 1s':
		btn_wnd_rr["text"] = "reroll all"
	else:
		btn_wnd_rr["text"] = "reroll off"
def def_w_rr():
	if btn_wnd_rr["text"] == "reroll once":
		return "reroll off"
	elif btn_wnd_rr["text"] == "reroll twice":
		return "reroll off"
	elif btn_wnd_rr["text"] == "reroll thrice":
		return "reroll off"
	else:
		return btn_wnd_rr["text"]
def fct_6eap():
	if btn_6eap["text"] == '0 AP on 6':
		btn_6eap["text"] = "-1 AP on 6"
	elif btn_6eap["text"] == '-1 AP on 6':
		btn_6eap["text"] = "-2 AP on 6"
	elif btn_6eap["text"] == '-2 AP on 6':
		btn_6eap["text"] = "-3 AP on 6"
	elif btn_6eap["text"] == '-3 AP on 6':
		btn_6eap["text"] = "-4 AP on 6"
	else:
		btn_6eap["text"] = "0 AP on 6"
def fct_hit_ed6():
	if btn_ed6["text"] == '+0 D on 6':
		btn_ed6["text"] = '+1 D on 6'
	else:
		btn_ed6["text"] = '+0 D on 6'
def fct_hit_mw6():
	if btn_mw6["text"] == '6 no mw':
		btn_mw6["text"] = "6 1 mw"
	elif btn_mw6["text"] == '6 1 mw':
		btn_mw6["text"] = "6 2 mw"
	elif btn_mw6["text"] == '6 2 mw':
		btn_mw6["text"] = "6 D3 mw"
	elif btn_mw6["text"] == '6 D3 mw':
		btn_mw6["text"] = "6 D6 mw"
	else:
		btn_mw6["text"] = "6 no mw"
def fct_sv_rr():
	if btn_sv_rr["text"] == 'reroll off':
		btn_sv_rr["text"] = "reroll once"
	elif btn_sv_rr["text"] == "reroll once":
		btn_sv_rr["text"] = "reroll twice"
	elif btn_sv_rr["text"] == "reroll twice":
		btn_sv_rr["text"] = "reroll thrice"
	elif btn_sv_rr["text"] == "reroll thrice":
		btn_sv_rr["text"] = "reroll 1s"
	elif btn_sv_rr["text"] == 'reroll 1s':
		btn_sv_rr["text"] = "reroll all"
	else:
		btn_sv_rr["text"] = "reroll off"
def def_s_rr():
	if btn_sv_rr["text"] == "reroll once":
		return "reroll off"
	elif btn_sv_rr["text"] == "reroll twice":
		return "reroll off"
	elif btn_sv_rr["text"] == "reroll thrice":
		return "reroll off"
	else:
		return btn_sv_rr["text"]
def fct_d_int():
	if btn_d_int["text"] == 'd int off':
		btn_d_int["text"] = "d int on"
		btn_d_d3["text"] = "d d3 off"
		btn_d_d6["text"] = "d d6 off"
		btn_rr_d["text"] = "reroll d off"
		d_int["text"] = 1
		min_d_int["text"] = 1
def fct_d_d3():
	if btn_d_d3["text"] == 'd d3 off':
		btn_d_d3["text"] = "d d3"
		btn_d_int["text"] = "d int off"
		btn_d_d6["text"] = "d d6 off"
		d_int["text"] = 0
	elif btn_d_d3["text"] == 'd d3':
		btn_d_d3["text"] = "d 2d3"
	elif btn_d_d3["text"] == 'd 2d3':
		btn_d_d3["text"] = "d 3d3"
	else:
		btn_d_d3["text"] = "d d3 off"
		btn_d_int["text"] = "d int on"
		d_int["text"] = 1
		min_d_int["text"] = 1
		btn_rr_d["text"] = "reroll d off"
def fct_d_d6():
	if btn_d_d6["text"] == 'd d6 off':
		btn_d_d6["text"] = "d d6"
		btn_d_d3["text"] = "d d3 off"
		btn_d_int["text"] = "d int off"
		d_int["text"] = 0
	elif btn_d_d6["text"] == 'd d6':
		btn_d_d6["text"] = "d 2d6"
	else:
		btn_d_d6["text"] = "d d6 off"
		btn_rr_d["text"] = "reroll d off"
		btn_d_int["text"] = "d int on"
		d_int["text"] = 1
		min_d_int["text"] = 1
def fct_d_co():
	if btn_d_co["text"] == 'd carry off':
		btn_d_co["text"] = "d carry on"
	else:
		btn_d_co["text"] = 'd carry off'
def fct_fnp():
	if btn_d_fnp["text"] == 'fnp off':
		btn_d_fnp["text"] = "fnp 6"
		btn_d_fnp_mw["text"] = "fnp mw 6"
	elif btn_d_fnp["text"] == 'fnp 6':
		btn_d_fnp["text"] = "fnp 5"
		btn_d_fnp_mw["text"] = "fnp mw 5"
	elif btn_d_fnp["text"] == 'fnp 5':
		btn_d_fnp["text"] = "fnp 4"
		btn_d_fnp_mw["text"] = "fnp mw 4"
	else:
		btn_d_fnp["text"] = "fnp off"
		btn_d_fnp_mw["text"] = "fnp mw off"
def fct_fnp_mw():
	if btn_d_fnp_mw["text"] == 'fnp mw off':
		btn_d_fnp_mw["text"] = "fnp mw 6"
	elif btn_d_fnp_mw["text"] == 'fnp mw 6':
		btn_d_fnp_mw["text"] = "fnp mw 5"
	elif btn_d_fnp_mw["text"] == 'fnp mw 5':
		btn_d_fnp_mw["text"] = "fnp mw 4"
	else:
		btn_d_fnp_mw["text"] = "fnp mw off"
def fct_rr_d():
	if btn_rr_d["text"] == 'reroll d off' and btn_d_int["text"] != 'd int on':
		btn_rr_d["text"] = "reroll d on"
	else:
		btn_rr_d["text"] = "reroll d off"
##reader for entries
def intial_attacks():
	if ''.join(i for i in entry_attacks.get() if ord(i) >=48 and ord(i) <= 59) == '':
		return 0
	else:
		return int(''.join(i for i in entry_attacks.get() if ord(i) >=48 and ord(i) <= 59))
def exp_attacks():
	if btn_exp["text"] == "explode off":
		return 0
	else:
		return int(btn_exp["text"][-1])
def exp_attacks_on():
	if btn_exp["text"] == "explode off":
		return 0
	elif int(btn_exp["text"][0]) < int(bs_int["text"]):
		return (7-int(bs_int["text"]))/6
	else:
		return (7-int(btn_exp["text"][0]))/6
def extra_damage_6():
	return(int(btn_ed6["text"][1]))
def number_of_enemies():
	if ''.join(i for i in entry_noe.get() if ord(i) >=48 and ord(i) <= 59) == '':
		return 0
	else:
		return int(''.join(i for i in entry_noe.get() if ord(i) >=48 and ord(i) <= 59))
def w():
	if ''.join(i for i in entry_w.get() if ord(i) >=48 and ord(i) <= 59) == '':
		return 0
	else:
		return int(''.join(i for i in entry_w.get() if ord(i) >=48 and ord(i) <= 59))
def max_mw():
	if ''.join(i for i in entry_mmw.get() if ord(i) >=48 and ord(i) <= 59) == '':
		return 0
	else:
		return int(''.join(i for i in entry_mmw.get() if ord(i) >=48 and ord(i) <= 59))
##functions for monte carlo sim
def start():
	lh, lws, ls, ld, j = [], [], [], [], 0
	bs, blst, exp, exp_int, exp_on = (7-int(bs_int["text"]))/6, btn_blst["text"], btn_exp["text"], exp_attacks(), exp_attacks_on()
	dak, flm, hit_rr, h6iw = btn_dka["text"], btn_flm["text"], def_h_rr(), btn_h6iw["text"]
	wnd, wnd_rr, mmw, mwo6, ed6 = (7-int(w_int["text"]))/6, def_w_rr(), max_mw(), btn_mw6["text"], extra_damage_6()
	sav, sv_rr = (7-int(sv_int["text"]))/6, def_s_rr()
	sv_eap, noe, lw1, ia = (sav + (int(btn_6eap["text"][0:2]))/6), number_of_enemies(), [w()]*number_of_enemies(), intial_attacks()
	dam_int, dam_d3, dam_d6, dam_min, dam_add = int(d_int["text"]), btn_d_d3["text"], btn_d_d6["text"], int(min_d_int["text"]), int(d_add_int["text"])
	rr_d, fnp, fnp_mw, d_co = btn_rr_d["text"], btn_d_fnp["text"], btn_d_fnp_mw["text"], btn_d_co["text"]

	while j < 10000:
		lw, dict_0, dict_1 = lw1, {"lmw": 0, "leapad": 0, "l6hiw":0,}, rr_one()
		if blst == 'blast off':
			attacks = ia
		else:
			attacks = sum(((shots_blast(noe, blst))) for i in range (0, ia))
		hits = sum((hitting(exp, bs, flm, dak, hit_rr, exp_int, exp_on, h6iw, dict_0, dict_1)) for i in range (0, attacks))
		lh.append(hits+dict_0["l6hiw"])
		wounds = sum((wounding(wnd, wnd_rr, mwo6, dict_0, dict_1)) for i in range(0, hits))
		lws.append(wounds+dict_0["leapad"]+dict_0["l6hiw"])
		saves = sum((save(sav, sv_rr, dict_1)) for i in range(0, wounds+dict_0["l6hiw"]))
		saves2 = sum(save2(sv_eap, sv_rr, dict_1) for i in range(0, dict_0["leapad"]))
		ls.append(saves+saves2)
		mwd = sum(mw_number(mwo6) for i in range(0, dict_0["lmw"]))
		lw = damage_mw(mwd, lw, mmw, fnp_mw, mwo6)
		for i in range(0, saves):
			lw = damage(lw, dam_int, dam_d3, dam_d6, rr_d, dam_min, dam_add, d_co, fnp)
		for i in range(0, saves2):
			lw = damage2(lw, dam_int, dam_d3, dam_d6, rr_d, dam_min, dam_add, d_co, fnp, ed6)
		remaining = sum(lw)
		ld.append(remaining)
		j += 1
	avg_hit_int["text"] = round(mean(lh))
	stdev_hit_int["text"] = round(stdev(lh))
	avg_w_int["text"] = round(mean(lws))
	stdev_w_int["text"] = round(stdev(lws))
	avg_sv_int["text"] = round(mean(ls))
	stdev_sv_int["text"] = round(stdev(ls))
	avg_d_int["text"] = round(sum(lw1) - mean(ld))
	stdev_d_int["text"] = round(stdev(ld)) 
	percent_remaining["text"] = f'{min_expect(lw1, ld)} - {max_expect(lw1, ld)}'

##layout of GUI
window = tk.Tk()
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], minsize=10, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=75, weight=1)
title = tk.Label(master=window, text="40Kalculator Alpha MKI Edition", font='Helvetica 18 bold', anchor="w")
title.grid(row=0, column=0, columnspan=7, sticky="ew")

##shooting GUI
sub_title_shooting = tk.Label(master=window, text="Hitting", font='Helvetica 14', anchor="w")
sub_title_shooting.grid(row=2, column=0, columnspan=2, sticky="ew")
lable_shoot = tk.Label(master=window, text="attacks")
lable_shoot.grid(row=3, column=0, sticky="nsew")
entry_attacks = tk.Entry()
entry_attacks.grid(row=3, column=1, columnspan=2)
btn_hit = tk.Button(master=window, text="reroll off", command=fct_hit_rr)
btn_hit.grid(row=3, column=3, sticky="nsew")
CreateToolTip(btn_hit, text = 'Re-rolls certain failed hits')
btn_exp = tk.Button(master=window, text="explode off", command=fct_hit_exp)
btn_exp.grid(row=3, column=4, sticky="nsew")
CreateToolTip(btn_exp, text = '6 generate extra hits\n' 'Example: Necron Telsa')
btn_dka = tk.Button(master=window, text="dakka off", command=fct_hit_dakka)
btn_dka.grid(row=3, column=5, sticky="nsew")
CreateToolTip(btn_dka, text = '6 generate shots that still need to hit\n''Example: Imperial Fists bolters')
btn_flm = tk.Button(master=window, text="flame off", command=fct_hit_flm)
btn_flm.grid(row=3, column=6, sticky="nsew")
CreateToolTip(btn_flm, text = 'Rolls to generate number of auto hits\n''Example: Every flamer weapon')
btn_blst = tk.Button(master=window, text="blast off", command=fct_hit_blst)
btn_blst.grid(row=3, column=7, sticky="nsew")
CreateToolTip(btn_blst, text = 'Random number of hits made\n' 'Blast being on adds min shots.\n''Example: Missle Launcher Frag')
btn_h6iw = tk.Button(master=window, text="6 wound off", command=fct_hit_h6iw)
btn_h6iw.grid(row=3, column=8, sticky="nsew")
CreateToolTip(btn_h6iw, text = '6 generates a wound instead of a hit\n''Example: Necron Canoptek Scarabs')

sub_title_bs = tk.Label(master=window, text="BS/WS")
sub_title_bs.grid(row=4, column=1)
btn_bs_minus = tk.Button(master=window, text="-", command=decr_bs)
btn_bs_minus.grid(row=5, column=0, sticky="nsew")
bs_int = tk.Label(master=window, text="4")
bs_int.grid(row=5, column=1)
btn_bs_add = tk.Button(master=window, text="+", command=incr_bs)
btn_bs_add.grid(row=5, column=2, sticky="nsew")

##wounding GUI
sub_title_Wounding = tk.Label(master=window, text="Wounding", font='Helvetica 14', anchor="w")
sub_title_Wounding.grid(row=6, column=0, columnspan=2, sticky="ew")
btn_wnd_rr = tk.Button(master=window, text="reroll off", command=fct_w_rr)
btn_wnd_rr.grid(row=7, column=4, sticky="nsew")
lable_mmw = tk.Label(master=window, text="max mortal wounds")
lable_mmw.grid(row=7, column=0, columnspan=2, sticky="nsew")
entry_mmw = tk.Entry()
entry_mmw.grid(row=7, column=2, columnspan=2)
CreateToolTip(btn_wnd_rr, text = 'Re-rolls certain failed wounds')
btn_6eap = tk.Button(master=window, text="0 AP on 6", command=fct_6eap)
btn_6eap.grid(row=7, column=5, sticky="nsew")
CreateToolTip(btn_6eap, text = '6 generates a save at an additional AP\n''Example: Tau Through Unity Devistation')
btn_ed6 = tk.Button(master=window, text="+0 D on 6", command=fct_hit_ed6)
btn_ed6.grid(row=7, column=6, sticky="nsew")
CreateToolTip(btn_ed6, text = '6 generates extra damage\n''Example: Incubi Lethal Precision')
btn_mw6 = tk.Button(master=window, text="6 no mw", command=fct_hit_mw6)
btn_mw6.grid(row=7, column=7, sticky="nsew")
CreateToolTip(btn_mw6, text = '6 generates a mortal wound\n''Example: Admech Wrath of Mars')

wounds_on = tk.Label(master=window, text="wounds on")
wounds_on.grid(row=8, column=1)
btn_w_minus = tk.Button(master=window, text="-", command=decr_w)
btn_w_minus.grid(row=9, column=0, sticky="nsew")
w_int = tk.Label(master=window, text="4")
w_int.grid(row=9, column=1)
btn_w_add = tk.Button(master=window, text="+", command=incr_w)
btn_w_add.grid(row=9, column=2, sticky="nsew")

##saving GUI
sub_title_Saving = tk.Label(master=window, text="Saving", font='Helvetica 14', anchor="w")
sub_title_Saving.grid(row=10, column=0, columnspan=2, sticky="ew")
lable_enemy = tk.Label(master=window, text="number of enemies")
lable_enemy.grid(row=11, column=0, columnspan=2, sticky="nsew")
entry_noe = tk.Entry()
entry_noe.grid(row=11, column=2, columnspan=2)
lable_w = tk.Label(master=window, text="wounds per enemy")
lable_w.grid(row=11, column=4, columnspan=2, sticky="nsew")
entry_w = tk.Entry()
entry_w.grid(row=11, column=6, columnspan=2)
btn_sv_rr = tk.Button(master=window, text="reroll off", command=fct_sv_rr)
btn_sv_rr.grid(row=11, column=8, sticky="nsew")
CreateToolTip(btn_sv_rr, text = 'Re-rolls certain failed saves')

saves_on = tk.Label(master=window, text="saves on")
saves_on.grid(row=12, column=0, columnspan=3, sticky="nsew")
btn_sv_minus = tk.Button(master=window, text="-", command=decr_sv)
btn_sv_minus.grid(row=13, column=0, sticky="nsew")
sv_int = tk.Label(master=window, text="4")
sv_int.grid(row=13, column=1)
btn_sv_add = tk.Button(master=window, text="+", command=incr_sv)
btn_sv_add.grid(row=13, column=2, sticky="nsew")

##damage GUI
sub_title_Damage = tk.Label(master=window, text="Damage", font='Helvetica 14', anchor="w")
sub_title_Damage.grid(row=14, column=0, columnspan=2, sticky="ew")

btn_d_int = tk.Button(master=window, text="d int on", command=fct_d_int)
btn_d_int.grid(row=15, column=1, sticky="nsew")
CreateToolTip(btn_d_int, text = 'Uses selected integer damage instead of random')
btn_d_d3 = tk.Button(master=window, text="d d3 off", command=fct_d_d3)
btn_d_d3.grid(row=15, column=2, sticky="nsew")
CreateToolTip(btn_d_d3, text = 'Uses random D3 damage instead of set integer')
btn_d_d6 = tk.Button(master=window, text="d d6 off", command=fct_d_d6)
btn_d_d6.grid(row=15, column=3, sticky="nsew")
CreateToolTip(btn_d_d6, text = 'Uses random D6 damage instead of set integer')
btn_rr_d = tk.Button(master=window, text="reroll d off", command=fct_rr_d)
btn_rr_d.grid(row=15, column=4, sticky="nsew")
CreateToolTip(btn_rr_d, text = 'Re-rolls damage and selects the higher of the two\n''Example: Old Melta weapons')
btn_d_co = tk.Button(master=window, text="d carry off", command=fct_d_co)
btn_d_co.grid(row=15, column=5, sticky="nsew")
CreateToolTip(btn_d_co, text = 'Damage carries over to next model\n''Example: Dark Angles Flail of the Unforgiven ')
btn_d_fnp = tk.Button(master=window, text="fnp off", command=fct_fnp)
btn_d_fnp.grid(row=15, column=6, sticky="nsew")
CreateToolTip(btn_d_fnp, text = 'Ignores each point of damage if rolled above\n''Example: Space Marine Apothecary ')
btn_d_fnp_mw = tk.Button(master=window, text="fnp mw off", command=fct_fnp_mw)
btn_d_fnp_mw.grid(row=15, column=7, sticky="nsew")
CreateToolTip(btn_d_fnp_mw, text = 'Same as FNP but only on mortal wounds\n''Example: Space Marine Black Templars')

lable_d_int = tk.Label(master=window, text="damage integer")
lable_d_int.grid(row=16, column=0, columnspan=3, sticky="nsew")
btn_d_int_minus = tk.Button(master=window, text="-", command=decr_d_int)
btn_d_int_minus.grid(row=17, column=0, sticky="nsew")
d_int = tk.Label(master=window, text="1")
d_int.grid(row=17, column=1)
btn_d_int_plus = tk.Button(master=window, text="+", command=incr_d_int)
btn_d_int_plus.grid(row=17, column=2, sticky="nsew")

lable_d_add_d = tk.Label(master=window, text="additional damage")
lable_d_add_d.grid(row=16, column=3, columnspan=3, sticky="nsew")
btn_d_add_minus = tk.Button(master=window, text="-", command=decr_d_add)
btn_d_add_minus.grid(row=17, column=3, sticky="nsew")
d_add_int = tk.Label(master=window, text="0")
d_add_int.grid(row=17, column=4)
btn_d_add_plus = tk.Button(master=window, text="+", command=incr_d_add)
btn_d_add_plus.grid(row=17, column=5, sticky="nsew")

lable_min_d = tk.Label(master=window, text="min damage")
lable_min_d.grid(row=16, column=6, columnspan=3, sticky="nsew")
btn_min_d_minus = tk.Button(master=window, text="-", command=decr_d_min)
btn_min_d_minus.grid(row=17, column=6, sticky="nsew")
min_d_int = tk.Label(master=window, text="1")
min_d_int.grid(row=17, column=7)
btn_min_d_plus = tk.Button(master=window, text="+", command=incr_d_min)
btn_min_d_plus.grid(row=17, column=8, sticky="nsew")

##averages/stdev GUI
avg_hit = tk.Label(master=window, relief=tk.RIDGE, text="Avg Hitting", font='Helvetica 12')
avg_hit.grid(row=2, column=9, columnspan=2, sticky="nsew")
avg_hit_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
avg_hit_int.grid(row=3, column=9, columnspan=2, sticky="nsew")
stdev_hit = tk.Label(master=window, relief=tk.RIDGE, text="Stdev Hitting", font='Helvetica 12')
stdev_hit.grid(row=4, column=9, columnspan=2, sticky="nsew")
stdev_hit_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
stdev_hit_int.grid(row=5, column=9, columnspan=2, sticky="nsew")

avg_w = tk.Label(master=window, relief=tk.RIDGE, text="Avg Wounding", font='Helvetica 12')
avg_w.grid(row=6, column=9, columnspan=2, sticky="nsew")
avg_w_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
avg_w_int.grid(row=7, column=9, columnspan=2, sticky="nsew")
stdev_w = tk.Label(master=window, relief=tk.RIDGE, text="Stdev Wounding", font='Helvetica 12')
stdev_w.grid(row=8, column=9, columnspan=2, sticky="nsew")
stdev_w_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
stdev_w_int.grid(row=9, column=9, columnspan=2, sticky="nsew")

avg_sv = tk.Label(master=window, relief=tk.RIDGE, text="Avg Sv Failed", font='Helvetica 12')
avg_sv.grid(row=10, column=9, columnspan=2, sticky="nsew")
avg_sv_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
avg_sv_int.grid(row=11, column=9, columnspan=2, sticky="nsew")
stdev_sv = tk.Label(master=window, relief=tk.RIDGE, text="Stdev Sv Failed", font='Helvetica 12')
stdev_sv.grid(row=12, column=9, columnspan=2, sticky="nsew")
stdev_sv_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
stdev_sv_int.grid(row=13, column=9, columnspan=2, sticky="nsew")

avg_d = tk.Label(master=window, relief=tk.RIDGE, text="Avg Damage", font='Helvetica 12')
avg_d.grid(row=14, column=9, columnspan=2, sticky="nsew")
avg_d_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
avg_d_int.grid(row=15, column=9, columnspan=2, sticky="nsew")
stdev_d = tk.Label(master=window, relief=tk.RIDGE, text="Stdev Damage", font='Helvetica 12')
stdev_d.grid(row=16, column=9, columnspan=2, sticky="nsew")
stdev_d_int = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
stdev_d_int.grid(row=17, column=9, columnspan=2, sticky="nsew")

time_remaining = tk.Label(master=window, relief=tk.RIDGE, text="Expect Damage", font='Helvetica 12')
time_remaining.grid(row=19, column=9, columnspan=2, sticky="nsew")
percent_remaining = tk.Label(master=window, relief=tk.RIDGE, text="0", font='Helvetica 12')
percent_remaining.grid(row=20, column=9, columnspan=2, sticky="nsew")

btn_start = tk.Button(master=window, text="S T A R T", font='Helvetica 18 bold', command=start)
btn_start.grid(row=19, column=2, rowspan=2, columnspan= 5, sticky="nsew")

window.mainloop()