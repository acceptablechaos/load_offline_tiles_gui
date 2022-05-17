# Gui to work as a companion to the TkinterMapView built by TomSchimansky
# https://github.com/TomSchimansky/TkinterMapView

import tkintermapview
import tkinter as tk
import os

root = tk.Tk()
root.title('Tile Download')
canvas1 = tk.Canvas(root, width = 300, height = 280, bg="light green")
canvas1.pack()
canvas1.create_text(150,30, text="Top Left", font="Times", fill="black")
entry1 = tk.Entry (root)
canvas1.create_window(80, 55, window=entry1)
entry2 = tk.Entry (root)
canvas1.create_window(220, 55, window=entry2)
canvas1.create_text(150,100, text="Bottom Right", font="Times", fill="black")
entry3 = tk.Entry (root)
canvas1.create_window(80, 125, window=entry3)
entry4 = tk.Entry (root)
canvas1.create_window(220, 125, window=entry4)
canvas1.create_text(150,170, text="Input File Name Ending In .db", font="Times", fill="black")
entry5 = tk.Entry (root)
canvas1.create_window(150, 195, window=entry5)

def ShowMe():
  input1 = entry1.get()
  input2 = entry2.get()
  input3 = entry3.get()
  input4 = entry4.get()
  file_name = entry5.get()
  zooms = zoom_var.get()
  clean1 = eval(input1)
  clean2 = eval(input2)
  clean3 = eval(input3)
  clean4 = eval(input4)
  grid1 = (clean1,clean2)
  grid2 = (clean3,clean4)
  level = eval(zooms)
 
# specify the region to load (New York City)
  top_left_position = (grid1)
  bottom_right_position = (grid2)
  zoom_min = 0
  zoom_max = (level)

# specify path and name of the database
  script_directory = os.path.dirname(os.path.abspath(__file__))
  database_path = os.path.join(script_directory, (file_name))

# create OfflineLoader instance
  loader = tkintermapview.OfflineLoader(path=database_path)

# save the tiles to the database, an existing database will extended
  loader.save_offline_tiles(top_left_position, bottom_right_position, zoom_min, zoom_max)


# print all regions that were loaded in the database
  loader.print_loaded_sections()
zoomzoom = [*range(1,18)]
zoom_var = tk.StringVar(root)
zoom_var.set("Zoom Level")
Zoom = tk.OptionMenu(root, zoom_var, *zoomzoom).place(x=45, y=225)

printbutton = tk.Button(root, text="Get Tiles", command=ShowMe)
printbutton.place(x=185, y=226)


root.mainloop()
