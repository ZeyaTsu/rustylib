import sys, os
from .Rusty import Rusty

class Kon:
    def __init__(self, filename):
        if filename.endswith('.k-on'):
            if not os.path.isfile(filename):
                print(f"Rusty Help - {filename} doesn't exist, making one...")
                self.fileS = filename
                self.mkKonDefault(self.fileS)
            self.fileS = filename
        else:
            print("Rusty Error - Rkon only accepts .k-on extension.")
            sys.exit()

    def mkKon(self, name):
        if name.endswith('.k-on'):
            pass
        else:
            name = f"{name}.k-on"
        with open(name, 'w') as f:
            pass
    
    def mkKonDefault(self, name):
        if name.endswith('.k-on'):
            pass
        else:
            name = f"{name}.k-on"
        with open(name, 'w') as f:
            df = [
                    "[DEFAULT]",
                    "isExample = True",
                    "Number = 1",
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