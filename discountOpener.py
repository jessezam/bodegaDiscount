import webbrowser
import time
import os

file = "\\list.txt"
path = os.getcwd()+file
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
while(1):
    with open(path, 'r') as f:
        lines = f.readlines()
    with open(path, "w") as f:
        current_line = 1
        for line in lines:
            if(current_line == 1):
                url = line
                print("Trying url: " + url)
            else:
                f.write(line)
            current_line += 1
    webbrowser.get('chrome').open_new_tab(url)
    time.sleep(6)