import requests
import keyring
from colorama import init, Fore
import os
import time
import requests
import hashlib
import platform
import subprocess
from pyupdater.client import Client
from pyupdater.client import AppUpdate
from pyupdater.client import FileDownloader

client = Client("https://github.com/Alpha-Tool/alpha-tool.git")

def main_menu():
    while True:
        os.system('cls')
        os.system('cls')
        os.system('cls')
        os.system('cls')
        os.system('cls')
        print(colored_ascii_art)
        print("Main Menu:")
        print(" ")
        print("[1] - MODE WTB/WTS    [2] - J1GG                [3] - Views Vinted")
        print(" ")
        print("[4] - SETTINGS        [5] - SOON...             [6] - SOON...")
        print(" ")
        print("[7] - SOON...         [8] - Exit")
        print(" ")
        print(" ")
        choix = input(CY + "Enter your choice : " + END)

        if choix == "1":
            os.system('cls')
            print(colored_ascii_art)
            mode_wta()
        elif choix == "2":
            os.system('cls')
            print(colored_ascii_art)
            main_menu()
        elif choix == "3":
              os.system('cls')
              print(colored_ascii_art)
              main_menu()
        elif choix == "4":
              os.system('cls')
              print(colored_ascii_art)
              settings()
        elif choix == "5":
              os.system('cls')
              print(colored_ascii_art)
              main_menu() 
        elif choix == "6":
              os.system('cls')
              print(colored_ascii_art)
              main_menu()
        elif choix == "7":
              os.system('cls')
              print(colored_ascii_art)
              main_menu()
        elif choix == "8":
            os.system('cls')
            print(colored_ascii_art)
            print(RED +"\n\n\n\n\n\nProgram closing..." + END)
            time.sleep(4)
            exit()
        else:
            print("Invalid choice.")

appdata_path = os.getenv('APPDATA')
alpha_tool_path = os.path.join(appdata_path, 'AlphaTool')

if not os.path.exists(alpha_tool_path):
        os.makedirs(alpha_tool_path)

        # Create the .txt files inside the AlphaTool folder
        wts_path = os.path.join(alpha_tool_path, 'wts.txt')
        with open(wts_path, 'w', encoding='utf-8') as f:
            f.write('past your wts list here')

        wtb_path = os.path.join(alpha_tool_path, 'wtb.txt')
        with open(wtb_path, 'w', encoding='utf-8') as f:
            f.write('past your wtb list here')
            
        wtbid_path = os.path.join(alpha_tool_path, 'wtb_ids.txt')
        with open(wtbid_path, 'w', encoding='utf-8') as f:
            f.write('past your wtb id channel here')

        wtsid_path = os.path.join(alpha_tool_path, 'wts_ids.txt')
        with open(wtsid_path, 'w', encoding='utf-8') as f:
            f.write('past your wts id channel here')
else:
        # Check if the text files exist, and create them if they don't
        wts_path = os.path.join(alpha_tool_path, 'wts.txt')
        if not os.path.exists(wts_path):
            with open(wts_path, 'w', encoding='utf-8') as f:
                f.write('past your wts list here')
        
        wtb_path = os.path.join(alpha_tool_path, 'wtb.txt')
        if not os.path.exists(wtb_path):
            with open(wtb_path, 'w', encoding='utf-8') as f:
                f.write('past your wtb list here')
            
        wtbid_path = os.path.join(alpha_tool_path, 'wtb_ids.txt')
        if not os.path.exists(wtbid_path):
            with open(wtbid_path, 'w', encoding='utf-8') as f:
                f.write('past your wtb id channel here')

        wtsid_path = os.path.join(alpha_tool_path, 'wts_ids.txt')
        if not os.path.exists(wtsid_path):
            with open(wtsid_path, 'w', encoding='utf-8') as f:
                f.write('past your wts id channel here')


def mode_wta():
    while True:
        os.system('cls')
        os.system('cls')
        os.system('cls')
        os.system('cls')
        os.system('cls')
        print(colored_ascii_art)
        print("Menu:")
        print(" ")
        print("[1] - WTB                     [2] - WTS                 [3] - WTS & WTB")
        print(" ")
        print("[4] - Edit Message WTS        [5] - Edit Message WTB    [6] - Edit ID CHANNEL WTB")
        print(" ")
        print("[7] - Edit ID CHANNEL WTS     [8] - Exit")
        print(" ")
        print(" ")
        choix = input(CY + "Enter your choice : " + END)

        if choix == "1":
            print(ORANGE + "\nLAUNCHING TASK 1\n"+ END)
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            print("\n")
            send_wtb_message()
        elif choix == "2":
            print(ORANGE + "\nLAUNCHING TASK 2\n"+ END)
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            print("\n")
            send_wts_message()
        elif choix == "3":
            print(ORANGE + "\nLAUNCHING TASK 3\n"+ END)
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            print("\n")
            send_wta_message()
        elif choix == "4":
            print("LAUNCHING TASK 4")
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            subprocess.Popen(['notepad.exe', wts_path]) 
            input("\nPress enter when finished to return to the menu...")
        elif choix == "5":
            print("LAUNCHING TASK 5")
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            subprocess.Popen(['notepad.exe', wtb_path])
            input("\nPress enter when finished to return to the menu...") 
        elif choix == "6":
            print("LAUNCHING TASK 6")
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            subprocess.Popen(['notepad.exe', wtbid_path])
            input("\nPress enter when finished to return to the menu...")
        elif choix == "7":
            print("LAUNCHING TASK 7")
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            subprocess.Popen(['notepad.exe', wtsid_path])
            input("\nPress enter when finished to return to the menu...")
        elif choix == "8":
            os.system('cls')
            print(colored_ascii_art)
            print(END +"\n\n\n\n\n\nGo back to main menu..." + END)
            time.sleep(4)
            os.system('cls')
            main_menu()
        else:
            print("Invalid choice.")

# Choix 1
def send_wts_message():
    os.system('cls')
    with open(wts_path, "r", encoding="utf-8") as f:
        message = f.read()

    message += "\n\n**Using Tool ||made by mm_ronald#0398||**"

    with open(wtsid_path, "r") as f:
        channel_ids = f.read().splitlines()

    print(ORANGE + "Sending message to Discord channels..." + END)
    time.sleep(2)
    header = {"Authorization": f"{token}", "Content-Type": "application/json"}
    for channel_id in channel_ids:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        data = {"content": message}
        r = requests.post(url, json=data, headers=header)
        if r.status_code == 200:
            print(GREEN + f"\nMessage sent to channel {channel_id}\n" + END)
            time.sleep(2)
        else:
            print(RED + f"\nError sending message to channel {channel_id}\n" + END)
            time.sleep(2)
    print(GREEN + "Script completed successfully. Thank you for using ALPHA TOOL!" + END)
    time.sleep(5)
# Choix 2
def send_wtb_message():
    os.system('cls')
    with open(wtb_path, "r", encoding="utf-8") as f:
        message = f.read()

    message += "\n\n**Using Tool ||made by mm_ronald#0398||**"

    with open(wtbid_path, "r") as f:
        channel_ids = f.read().splitlines()

    print(ORANGE + "Sending message to Discord channels..." + END)
    time.sleep(2)
    header = {"Authorization": f"{token}", "Content-Type": "application/json"}
    for channel_id in channel_ids:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        data = {"content": message}
        r = requests.post(url, json=data, headers=header)
        if r.status_code == 200:
            print(GREEN + f"\nMessage sent to channel {channel_id}\n" + END)
            time.sleep(2)
        else:
            print(RED + f"Error sending message to channel {channel_id}\n" + END)
            time.sleep(2)
    print(GREEN + "Script completed successfully. Thank you for using ALPHA TOOL!" + END)
    time.sleep(5)
# Choix 3
def send_wta_message():
    
    os.system('cls')
    with open(wts_path, "r", encoding="utf-8") as f:
        message_wts = f.read()

    with open(wtb_path, "r", encoding="utf-8") as f:
        message_wtb = f.read()

    message_wts += "\n\n**Using Tool ||made by mm_ronald#0398||**"
    message_wtb += "\n\n**Using Tool ||made by mm_ronald#0398||**"

    with open(wtsid_path, "r") as f:
        wts_channel_ids = f.read().splitlines()

    with open(wtbid_path, "r") as f:
        wtb_channel_ids = f.read().splitlines()

    token = keyring.get_password("discord_api", "token")

    print(ORANGE + "Sending message to Discord channels..." + END)

    header = {"Authorization": f"{token}", "Content-Type": "application/json"}
    for channel_id in wts_channel_ids:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        data = {"content": message_wts}
        r = requests.post(url, json=data, headers=header)
        if r.status_code == 200:
            print(GREEN + f"\nMessage sent to channel {channel_id}\n" + END)
        else:
            print(RED + f"Error sending message to channel {channel_id}\n" + END)

    for channel_id in wtb_channel_ids:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        data = {"content": message_wtb}
        r = requests.post(url, json=data, headers=header)
        if r.status_code == 200:
            print(GREEN + f"\nMessage sent to channel {channel_id}\n" + END)
            time.sleep(2)
        else:
            print(RED + f"\nError sending message to channel {channel_id}\n" + END)
            time.sleep(2)
    print(GREEN + "Script completed successfully. Thank you for using ALPHA TOOL!" + END)
    time.sleep(5)

def settings():
    while True:
        os.system('cls')
        os.system('cls')
        os.system('cls')
        os.system('cls')
        os.system('cls')
        print(colored_ascii_art)
        print("Menu:")
        print(" ")
        print("[1] - CHANGE TOKEN                     [2] - Goback To Main Menu")
        print(" ")
        print(" ")
        choix = input(CY + "Enter your choice : " + END)

        if choix == "1":
            print(ORANGE + "\nLAUNCHING TASK 1\n"+ END)
            time.sleep(2)
            os.system('cls')
            print(colored_ascii_art)
            print("\n")
            token = keyring.get_password("discord_api", "token")
            print("current token:\n\n" + token )
            token = input('\n\n\n\n\nEnter an other token: ')
            keyring.set_password("discord_api", "token", token)
        elif choix == "2":
            os.system('cls')
            print(colored_ascii_art)
            print(END +"\n\n\n\n\n\nGo back to main menu..." + END)
            time.sleep(4)
            os.system('cls')
            main_menu()
        else:
            print("Invalid choice.")

init()

ascii_art = """


___________________________  ________       ___________________________ 
___    |__  /___  __ \__  / / /__    |      ___  __/_  __ \_  __ \__  / 
__  /| |_  / __  /_/ /_  /_/ /__  /| |      __  /  _  / / /  / / /_  /  
_  ___ |  /___  ____/_  __  / _  ___ |      _  /   / /_/ // /_/ /_  /___
/_/  |_/_____/_/     /_/ /_/  /_/  |_|      /_/    \____/ \____/ /_____/
                                                                        
        
     Welcome to the ALPHA TOOL script! made by mm_ronald#0398     
     
                                                                    
"""

colored_ascii_art = Fore.CYAN + ascii_art + Fore.RESET
print(colored_ascii_art, flush=True)

GREEN = "\033[32m"
ORANGE = "\033[33m"
RED = "\033[31m"
VIOLET = "\033[35m"
END = "\033[0m"
CY = "\033[36m"

# Vérifiez s'il existe des mises à jour disponibles pour l'application
client.refresh()

# Installez la mise à jour s'il y en a une disponible
app_update = client.update_check("Alpha Tool", "1.0.0")
if app_update is not None:
    # Télécharger la mise à jour
    print(f"Téléchargement de la mise à jour {app_update.version}...")
    downloader = FileDownloader(client)
    downloader.download(app_update.files)

    # Installer la mise à jour
    print(f"Installation de la mise à jour {app_update.version}...")
    app = AppUpdate(client)
    app.install_restart()
else:
    # Aucune mise à jour n'est disponible
    os.system('cls')


def generate_hwid():
    return hashlib.sha256(platform.node().encode()).hexdigest().strip()

while True:
    license = keyring.get_password("system", "license")
    if not license:
        license = input("Please enter your license: ")
        keyring.set_password("system", "license", license)

    # Display loading screen
    print(ORANGE + "\n\n\nValidating license...\n\n" + END)
    time.sleep(5)

    url = f"https://api.whop.com/api/v2/memberships/{license}/validate_license"
    payload = {"metadata": {"HWID": generate_hwid()}}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer F_n-WzuPPiRkNFWJBiRjsgHsutLdd6ia572gnb5cuAg",
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    if "Please reset your key to use on a new machine" in response.text:
        print(RED + "Access Denied - License Active on another machine" +END)
        keyring.delete_password("system", "license")
        time.sleep(3)
        exit()
    elif response.status_code == 201:
        print(GREEN + "License validated successfully!\n" + END)
    else:
        print(RED + f"Unknown Response - {response.status_code} - {response.text}" + END)
        keyring.delete_password("system", "license")
        os._exit(1)

    token = keyring.get_password("discord_api", "token")
    if not token:
        token = input('Enter your Discord API token: ')
        keyring.set_password("discord_api", "token", token)
    
    time.sleep(2)
    main_menu()


        

    
