filename = "yes.txt"
with open(filename, "w", encoding="utf-8") as f:
    x = 'y'
    while x == 'y':  
        text_input = input('>>>')
        f.write(text_input+'\n')
        x = input("write? (y/n)")

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

print(text)