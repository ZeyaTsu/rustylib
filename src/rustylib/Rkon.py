import sys, os
from .Rusty import Rusty
from .Rrandom import Random

class Kon:
    def __init__(self, filename):
        if filename.endswith('.k-on') or filename.endswith('.lyco'):
            if not os.path.isfile(filename):
                print(f"Rusty Help - {filename} doesn't exist, making one...")
                self.fileS = filename
                self.mkKonDefault(self.fileS)
            self.fileS = filename
        else:
            print("Rusty Error - Rkon only accepts .k-on or .lyco extension. (You may want to change .ini to .k-on ?)")
            sys.exit()

    def mkKon(self, name):
        if name.endswith('.k-on'):
            pass
        else:
            name = f"{name}.k-on"
        with open(name, 'w') as f:
            pass
    
    def mkKonDefault(self, name):
        if name.endswith('.k-on') or name.endswith('.lyco'):
            pass
        else:
            name = f"{name}.k-on"
        rand = Random.init()
        with open(name, 'w') as f:
            df = [
                    "[DEFAULT]",
                    "isExample = True",
                    f"Number = {rand.rint(0, 100)}",
                    "string = Hello world!"
                ]
            for items in df:
                f.write(f"{items}\n")
        
    def read(self):
        data = {}
        current_section = None

        with open(self.fileS, "r") as f:
            for line in f:
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("//"):
                    continue

                # Check if line starts with a section header
                if line.startswith("[") and line.endswith("]"):
                    current_section = line[1:-1]
                    data[current_section] = {}
                    continue

                # Split key-value pair
                key, value = line.split("=", 1)

                # Add key-value pair to current section
                if current_section:
                    data[current_section][key.strip()] = value.strip()

        return data

    def isExisting(self, keywordItem, getLine=False):
        with open(self.fileS, "r") as f:
            i = 0
            for line in f:
                i+=1
                if keywordItem == line.strip():
                    if getLine == True:
                        return i
                    return True

            return False

    def insert(self, keywordsItem:list):
        for items in keywordsItem:
            with open(self.fileS, 'a') as f:
                if items.startswith('[') and items.endswith(']'):
                    f.write('\n')
                f.write(f"\n{items}")
    
    def remove(self, keywordsItem):
        with open(self.fileS, 'r') as f:
            lines = f.readlines()
        with open(self.fileS, 'w') as f:
            for line in lines:
                if keywordsItem not in line:
                    f.write(line)

class Secret:
    def secret_song():
        import os
        import random
        import pygame

        songs_with_names = {
            "kon.wav" : "Playing: Tenshi ni Fureta yo!",
        }

        # Choose a random song from the dictionary
        song_file = random.choice(list(songs_with_names.keys()))

        # Get the path to the song file in the same directory as this script
        file_path = os.path.join(os.path.dirname(__file__), song_file)

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Load the sound file
        sound = pygame.mixer.Sound(file_path)

        # Play the sound file
        print(f"Now playing {songs_with_names[song_file]}...")
        sound.play()

        # Wait for the sound to finish playing
        while pygame.mixer.get_busy():
            continue
