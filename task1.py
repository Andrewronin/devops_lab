import subprocess
import os
import yaml
import json

data = {}
with open('output.json', 'w') as file:
    json.dump(data, file)
with open('output.yaml', 'w') as file:
    yaml.dump(data, file)
answer = subprocess.run(["ls", "/home/student/.pyenv/versions"], capture_output=True).stdout
li = list(str(answer)[2:-3].split("\\n"))

for each in li:
    # 1 version
    path = "/home/student/.pyenv/versions/" + each
    bin_path = path + "/bin"
    if os.path.exists(bin_path + "/python2"):
        answer = subprocess.run([bin_path + "/python2", "-V"], capture_output=True).stderr
    if os.path.exists(bin_path + "/python3"):
        answer = subprocess.run([bin_path + "/python3", "-V"], capture_output=True).stdout
    data["Python version = "] = str(answer)[2:-3]

    # 2 Environment name
    data["Environment name = "] = each

    # 3 executable

    data["Exec path = "] = bin_path + "/python"

    # 4 pip location
    data["pip location = "] = bin_path + "/pip"

    # 5 PYTHONPATH
    if os.path.exists(bin_path + "/python2"):
        answer = subprocess.run([bin_path + "/python2", "-m", "site"], capture_output=True).stdout
    if os.path.exists(bin_path + "/python3"):
        answer = subprocess.run([bin_path + "/python3", "-m", "site"], capture_output=True).stdout
    answer = str(answer)[14:-154].replace("\\n", " ").replace("'", " ").replace("      /", "/")
    answer = answer.replace("'", " ")
    data["PYTHONPATH = "] = answer.split(",")

    # 6 Install packages
    os.system("pyenv local " + each)
    answer = subprocess.run(["pip", "freeze"], capture_output=True).stdout
    if answer:
        answer = str(answer)[2:-3].replace("\\", ", ").replace("==", " : ")
        data["Install packages = "] = answer.split(",")
    else:
        data["Install packages = "] = "No packages"

    # 7 Site packages
    answer = subprocess.run(["python", "-m", "site", "--user-site"], capture_output=True).stdout
    data["site-packages = "] = str(answer)[2:-3]
    print(data)
    with open('output.json', 'a') as file:
        json.dump(data, file, indent=4)
    with open('output.yaml', 'a') as file:
        yaml.dump(data, file)
