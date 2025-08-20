import os, shutil, re, requests

# 1. Move .jpg files
def move_jpg(source, target):
    if not os.path.exists(target):
        os.makedirs(target)
    for file in os.listdir(source):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(source, file), os.path.join(target, file))
            print("Moved:", file)
    print("All .jpg files moved!")

# 2. Extract emails from text file
def extract_emails(input_file, output_file):
    with open(input_file,"r") as f:
        data = f.read()
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", data)
    with open(output_file,"w") as f:
        for e in set(emails):
            f.write(e+"\n")
    print("Emails saved in", output_file)

# 3. Get webpage title
def get_title(url, output_file):
    html = requests.get(url).text
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    with open(output_file,"w") as f:
        f.write("Title: "+title)
    print("Title saved in", output_file)

# Main Menu
print("=== Automation Tool ===")
print("1. Move all .jpg files")
print("2. Extract emails from .txt file")
