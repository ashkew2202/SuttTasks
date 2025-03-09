getext = input("Enter the text: ")
import time

for i in range(len(getext)):
    if (getext[i] == ' '):
        print(getext[i], end='', flush=True)
        time.sleep(0.5)
    else:
        print(getext[i], end='', flush=True)
        time.sleep(0.05)

