import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Ipv4Screen(ttk.Frame):
    def __init__(self, parent, controller, show_ethernet_screen):
        super().__init__(parent)
        
        
        