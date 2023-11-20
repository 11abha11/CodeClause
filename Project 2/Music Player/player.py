import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
import threading
import pygame
import time
import os
from mutagen.mp3 import MP3


#initialize pygame mixer
pygame.mixer.init()

#storing position of the music progress
curr_pos = 0
paused = False
selected_folder = ""

def update_prog():
    global curr_pos
    while True:
        if pygame.mixer.music.get_busy() and not paused:
            curr_pos = pygame.mixer.music.get_pos()/1000
            progress_bar["value"] = curr_pos

            if curr_pos >= progress_bar["maximum"]:
                stop_music()
                progress_bar["value"] = 0

            root.update()
        time.sleep(0.1)

#thread to update progress bar
pt = threading.Thread(target = update_prog)
pt.daemon = True
pt.start()


#necessary command functions
def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    if selected_folder : 
        displayList.delete(0, tk.END)
        for filename in os.listdir(selected_folder):
            if filename.endswith(".mp3"):
                displayList.insert(tk.END , filename)

def previous_song():
    if len(displayList.curselection()) > 0:
        curr_index = displayList.curselection()[0]
        
        if curr_index > 0 :
            displayList.selection_clear(0, tk.END)
            displayList.selection_set(curr_index - 1)
            play_selected_song()

def play_song():
    global paused
    if paused:
        #unpause the music
        pygame.mixer.music.unpause()
        paused = False
    else:
        #play the song
        play_selected_song()

def play_selected_song():
    global curr_pos, selected_folder
    if len(displayList.curselection()) > 0 :
        curr_index = displayList.curselection()[0]
        selected_song = displayList.get(curr_index)
        path = os.path.join(selected_folder , selected_song)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(start = curr_pos)
        paused = False
        audio = MP3(path)
        duration = audio.info.length
        progress_bar["maximum"] = duration

def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_song():
    if len(displayList.curselection()) > 0:
        curr_index = displayList.curselection()[0]
        
        if curr_index < displayList.size() - 1:
            displayList.selection_clear(0, tk.END)
            displayList.selection_set(curr_index + 1)
            play_selected_song()

def stop_music():
    global paused 
    pygame.mixer.music.stop()
    paused = False


#creating the window
root = tk.Tk()
root.title("Music Player")
root.geometry("480x540")
root.config(background="lightblue")


#title
player_title = tk.Label(root, text="Music Player!", font=("Poppins", 25, "bold", "italic"),background="lightblue")
player_title.pack(pady=20)


#selecting music folder
select = ctk.CTkButton(root, text="Select Folder", command=select_folder, font=("Poppins", 15))
select.pack(pady=15)


#display list
displayList = tk.Listbox(root, width=50, font=("Poppins", 10))
displayList.pack(pady=15)


#frame for control buttons 
controlFrame = tk.Frame(root,background="lightblue")
controlFrame.pack(pady=20)


#previous button
prev_btn= tk.PhotoImage(file="Project 2\Music Player\prev_button.png")
width, height = 120, 120
prev_btn_resized = prev_btn.subsample(width // 10, height // 10)

previous = tk.Button(controlFrame, image=prev_btn_resized, command=previous_song, borderwidth=0, width=50,background="lightblue")
previous.pack(side=tk.LEFT, padx=5)


#play button
play_btn= tk.PhotoImage(file="Project 2\Music Player\play_button.png")
play_btn_resized = play_btn.subsample(width // 10, height // 10)


play = tk.Button(controlFrame, image=play_btn_resized, command=play_song, borderwidth=0, width=50, background="lightblue")
play.pack(side=tk.LEFT, padx=5)


#pause button
pause_btn= tk.PhotoImage(file="Project 2\Music Player\pause_button.png")
pause_btn_resized = pause_btn.subsample(width // 10, height // 10)


pause = tk.Button(controlFrame, image=pause_btn_resized, command=pause_song, borderwidth=0, width=50, background="lightblue")
pause.pack(side=tk.LEFT, padx=5)


#next button
next_btn= tk.PhotoImage(file="Project 2\Music Player\playNext_button.png")
next_btn_resized = next_btn.subsample(width // 10, height // 10)


next = tk.Button(controlFrame, image=next_btn_resized, command=next_song, borderwidth=0, width=50, background="lightblue")
next.pack(side=tk.LEFT, padx=5)


#progress bar
progress_bar = Progressbar(root, length=350, mode="determinate")
progress_bar.pack(pady=20)

root.mainloop()