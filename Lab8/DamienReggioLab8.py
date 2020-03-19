##
# Program Header:
# CIS 117 Python Programming: Lab #8
# Name: Damien Reggio
# Description: GUIS
# Application: Creating a Kilometer to Miles Converter
# Development Environment: Windows 7/Ubuntu 14.04
# Version: Python 3.7
# Filename: DamienReggioLab8.py
# Date: 3/19/2020

import tkinter as tk
import tkinter.messagebox
import re


class DistanceConvert(object):
    """GUI for converting between F and C
    """
    KM_TO_MILES = 0.621371

    def __init__(self):
        self.make_main_window()
        self.make_km_entry()
        self.make_miles_entry()
        self.make_exit_button()
        self.make_convert_button()
        # Start listening
        #
        tk.mainloop()

    def make_main_window(self):
        # Create main window
        #
        self.main_window = tk.Tk()
        self.main_window.geometry("300x200")

        # add label
        #
        self.label = tk.Label(self.main_window, text = 'Distance Conversion')

        # apply the label
        #
        self.label.pack()

    def make_convert_button(self):
        self.convert_button = tk.Button(master=self.main_window,
                                        text='Convert',
                                        command=self.convert)
        self.convert_button.pack(side=tk.RIGHT)

    def make_exit_button(self):
        self.quit_button = tk.Button(master=self.main_window,
                                     text='Exit',
                                     command=quit)
        self.quit_button.pack(side=tk.RIGHT, padx=10)

    def make_km_entry(self):
        """adds km entry box"""
        self.km_entry_label = tk.Label(master=self.main_window,
                                        text='Distance in km:')
        self.k_str = tk.StringVar()
        self.km_entry = tk.Entry(master=self.main_window,
                                 textvariable=self.k_str)
        self.km_entry_label.pack()
        self.km_entry.pack()
        # Watch variable for dynamic conversion
        #
        self.k_str.trace("w", self.dynamic_conversion)

    def make_miles_entry(self):
        """adds miles entry box"""
        self.m_entry_label = tk.Label(master=self.main_window,
                   text='Distance in miles:')
        self.m_str = tk.StringVar()
        self.m_entry = tk.Entry(master=self.main_window,
                                textvariable=self.m_str)
        self.m_entry_label.pack()
        self.m_entry.pack()
        # Watch variable for dynamic conversion
        #
        self.m_str.trace("w", self.dynamic_conversion)

    def dynamic_conversion(self, *args):
        """
        populates miles window as km window is populated and vice/versa
        """
        if self.main_window.focus_get() == self.km_entry:
            if self.km_entry.get():
                miles = self.km_to_m()
                if miles:
                    entry = miles
                else:
                    entry = 'invalid'
                self.m_entry.configure(state='normal')
                self.m_entry.delete(0, tk.END)
                self.m_entry.insert(0, entry)
                self.m_entry.configure(state='readonly')
            else:
                self.m_entry.configure(state='normal')
                self.m_entry.delete(0, tk.END)

        if self.main_window.focus_get() == self.m_entry:
            if self.m_entry.get():
                km = self.m_to_km()
                if km:
                    entry = km
                else:
                    entry = 'invalid'
                self.km_entry.configure(state='normal')
                self.km_entry.delete(0, tk.END)
                self.km_entry.insert(0, entry)
                self.km_entry.configure(state='readonly')
            else:
                self.km_entry.configure(state='normal')
                self.km_entry.delete(0, tk.END)

    def convert(self):
        """displays messagebox with km to m"""
        km = self.km_entry.get()
        miles = self.km_to_m()
        if miles:
            return_message = '{} km = {} miles'.format(km, miles)
        else:
            return_message = "Invalid entry, please enter a number"

        tk.messagebox.showinfo('Conversion:',
                               return_message)

    def km_to_m(self):
        """checks entry then converts km to m"""
        km = self.check_float(self.km_entry.get())
        if km:
            miles = km * self.KM_TO_MILES
            return round(miles, 2) if miles > 1 else round(miles, 6)
        else:
            return None

    def m_to_km(self):
        """checks entry then converts m to km"""
        miles = self.check_float(self.m_entry.get())
        if miles:
            km = miles / self.KM_TO_MILES
            return round(km, 2) if km > 1 else round(km, 6)
        else:
            return None

    @staticmethod
    def check_float(float_string):
        """
        checks if entry can be turned to a float returns as if possible float
        :param entry: a string
        :return: as a float or none
        """
        if re.match('^\d*\.?\d+$', float_string):
            return float(float_string)
        else:
            return None


def main():
    dist_convert = DistanceConvert()


if __name__ == '__main__':
    main()


# output
#
'''
see DamienReggioLab8demo.png
'''
