#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5e
#  in conjunction with Tcl version 8.6
#    May 27, 2022 06:09:10 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import pp75e_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'black':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    _style_code_ran = 1

class Toplevel1_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x545+895+367")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0,  0)
        top.title("ProperPath Demo")
        top.configure(highlightcolor="black")

        self.top = top
        self.LocalPath = tk.StringVar()
        self.ProperPath = tk.StringVar()

        self.btnExit = tk.Button(self.top)
        self.btnExit.place(x=450, y=20, height=33, width=113)
        self.btnExit.configure(activebackground="beige")
        self.btnExit.configure(borderwidth="2")
        self.btnExit.configure(command=pp75e_support.on_btnExit)
        self.btnExit.configure(compound='left')
        self.btnExit.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.btnExit.configure(text='''Exit''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(x=40, y=70, height=51, width=59)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(borderwidth="2")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Label''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(x=20, y=160, height=21, width=99)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='e')
        self.Label2.configure(compound='left')
        self.Label2.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label2.configure(text='''Local Path:''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(x=120, y=160, height=21, width=436)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(compound='left')
        self.Label3.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label3.configure(text='''Label''')
        self.Label3.configure(textvariable=self.LocalPath)
        self.LocalPath.set('''Label''')

        self.Label4 = tk.Label(self.top)
        self.Label4.place(x=20, y=200, height=21, width=99)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='e')
        self.Label4.configure(compound='left')
        self.Label4.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label4.configure(text='''Proper Path:''')

        self.Label5 = tk.Label(self.top)
        self.Label5.place(x=120, y=200, height=71, width=469)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='nw')
        self.Label5.configure(compound='left')
        self.Label5.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label5.configure(text='''Label''')
        self.Label5.configure(textvariable=self.ProperPath)
        self.ProperPath.set('''Label''')

        self.Label6 = tk.Label(self.top)
        self.Label6.place(x=120, y=70, height=51, width=59)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(borderwidth="2")
        self.Label6.configure(relief="groove")
        self.Label6.configure(text='''Label''')

        self.Label7 = tk.Label(self.top)
        self.Label7.place(x=125, y=10, height=51, width=59)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='w')
        self.Label7.configure(compound='left')
        self.Label7.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label7.configure(text='''Using Local Path''')
        self.Label7.configure(wraplength="70")

        self.Label8 = tk.Label(self.top)
        self.Label8.place(x=40, y=10, height=55, width=56)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(anchor='w')
        self.Label8.configure(compound='left')
        self.Label8.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label8.configure(text='''Using Proper Path''')
        self.Label8.configure(wraplength="70")

        _style_code()
        self.Scrolledtext1 = ScrolledText(self.top)
        self.Scrolledtext1.place(x=30, y=336, height=191, width=502)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(wrap="word")

        self.Label9 = tk.Label(self.top)
        self.Label9.place(x=30, y=307, height=21, width=259)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(anchor='w')
        self.Label9.configure(compound='left')
        self.Label9.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label9.configure(text='''All Path Variables:''')

        self.Label7_1 = tk.Label(self.top)
        self.Label7_1.place(x=203, y=12, height=51, width=89)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(anchor='w')
        self.Label7_1.configure(compound='left')
        self.Label7_1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label7_1.configure(text='''PAGE Embedded''')
        self.Label7_1.configure(wraplength="90")

        self.Label10 = tk.Label(self.top)
        self.Label10.place(x=215, y=70, height=51, width=59)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(borderwidth="2")
        photo_location = os.path.join(_location,"./images/icons/document.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label10.configure(image=_img0)
        self.Label10.configure(relief="groove")
        self.Label10.configure(text='''Label''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    pp75e_support.main()

if __name__ == '__main__':
    pp75e_support.main()




