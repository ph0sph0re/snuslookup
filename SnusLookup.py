import requests
import os

API_KEY = ''

MENU = """
　　　　　　　　　／:.:.:.:.:〃:.ミ:.:／:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.ヽ:.〃ヽ
　　　　　　　 ／:.:.:.:.:.:.ｲ:.l:.ミ:V:.:.:.:.:.:.:.:.:.:.:.:.:.:./:.:.:.:.:.:.:.:.ヽ:.:.:.:',
　　　　　　／:.:.:.:.:.:.:/　{八:.:/:.:.:.:.:.:.:.:.:.:.:.:.:イ:.:.:.:.:ﾊ:.:.:.:.:.:ヽ:.:.',
.　　　　／:.:.:.:.:.:.:.:./　　 ﾏ__l:.:.:.:.:.:.:.:.:.:.:／　l:.:.:.:./ ヽ:.:.:.:.:.ﾊ:.:.
.　 　／:.:.:.:.:.:.:.:.:.:/　　　|l::「l:./:.:.:.:.:.≠‐-　 j:.:./-‐-ヽ:.:.:.:.:.}:.:.:',
　　/:.:.:.:.:.:.:.:.:.:.:./　　　 |l::l::iｿ:.:.:.斥示ぅ　　ｲ:/斥ﾃｧ ﾊ:.:.:.:j:.:.:.:ﾊ
　 /:.:.:.:.:.:.:.:.:.:.:./　　　　ゞ=ﾑ:.イ:.i 込ｿ　 　j/　込ﾉ/:.}:.i:.:/:.:.:.:.:.ﾊ　　　　 __
　/:.:.:.:.r-v‐r､:{　　　　　　　jハ:.i､　　　　　,　 　 /ヽi:.:j/:.:.:.:.:.:.:.:ﾊ　 , ´:::::::｀ヽr‐== ､__
　:.:.:.:r ゝｲゝﾑ_ヽ　　　　Y´⌒｀ヽj＞　　ー　　 イ　 }:.:/ﾊ:.:.:.:.:.:.:.:.:.У::､::::::::::::::::ヽ≦､─‐-,
　:.:.:.:〉=x'´￣　｀ヽ　　　,'　　　 ,　｀＜＞-_≦-､-─jノ､　V:.:.:.:.:.:., ':::::::}::::::::::::::::::::ヽ::ヽ二ヽ__
　:.:.:.У':::::::::::::::::::::ヽ　　i　_＿　i　　　l}⌒ ヽ＼-ゝ-､　　>ﾑ:.:.:／:::::::::::i::::::::::::::::::::::::::ヽﾊ-─-'
　:.:.:.|l:::::::::::::::::::::::::::::ヽ f'´田:::｀x 人 /　　 /:.:./　､　 ￣ヽ:::::X::::::::::::::::.',:::::::::::::::::::::::::::::ヽﾄ､ヽ
　:.:.:.＼:::::::::::::::::::::::::::::ヽ::::::::::::::::::}　/ゝ__,ｲ:.:.:/　　 ゝ　　 .У::::::::::::::::::八:::::::::::::::::::::::::::::::ヽ=ｿ
　:.:.:.:.:.:＼::::::::::::::::::::::::::::ヽ､::::::::::::iノ　　/::.:.:/´　　　　｀　/:::::::::::::::::::::::::::::ゝ:::::::::::::::::::::::::::::ヽヽ
　:.:.:.:.:.:.:.:.:.＼::::::::::::::::::::::::::::ﾐ､::::::iヽ ／:.:.:.:/　　　　　　./:::::::::::::::::::::::::::::::::,'::::ヽ::::::::::::::::::::::::::ﾏ
　:.:.:.:.:.:.:.:.:.:.:.:.:＼:::::::::::::::::::::::V:::::j y:.:.:.:.:／　　　　　 r/:::::::::::::::::::::::::::::::::::,::::::::',:ヽ::::::::::::::::::::::, ､
　:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.＼:::::::::::::::::::::://:.:.:.:./ヽ　　　　　 ハ:::::::::::::::::::::::::::::::::::,::::::::::::',::::ヽ::::::::::::::::::' ,ヽ
ヽ :.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:｀　､::::::::://:.:.:.:./　　ヽ　／ rｿ:.:.}:::::::::::::::::::::::::::::::::,':::::::::::::::',:::::::ヽ:::::::::::::::ヽ:.:｀　､
　} :.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:ヽ=' 〈:.:.:.:.:{　　　 }´/::〃ﾊイゝ､::::::::::::::::::::::,.ﾑ:::::::::::::::::::',:::::::::ヽ:::::::::::::::ヽ:.:.:.:.:｀　､
　j :.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.ヽ　7:.:.:.:.|　　　.l/::〃::::}:./　　｀= _＿_ ='/:.:.}:::::::::::::::::::ﾊ::::::::::{=-:::r‐＝-､:.:.:.:.:.:.:.ヽ
. ﾉ :.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.ﾊ/:.:.:.:.::l　　 イ::〃j:::::Vi　　　　　　　　/>､ﾉ､:::::::::::::ｲ:.}::::::::::}::::::｀::::::::::::::{:.:.:.:.:.:.:.:.:.ヽ
　:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.|:.:.:.:／　 /:::ﾊ〃/／:.:.|　　　　　　　/:.／　 ｀ ￣´jヽﾑﾐ::::Y:::::::::::::::::::::::ヽ:.:.:.:.:.:.:.:.:.:ヽ
　:..:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:./l_／　 ／::::::〃ｿ´:.:.:／　　　　　　 /イ　　　　　　 ,'ｲ:::::｀:::::{::::::::::::::::::::::::::::ヽ:.:.:.:.:.:.:.:.:.:ヽ
　:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:..:.:.:.:／　　　 /／::::〃j/:.:.:./　　　　　　　 ,'.}　　　　　　　/:::::::::::::::::l:::::::::､:::::::::::::::::::::ヽ:..:.:.:.:.:.:.:.
　:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.／　　　　／￣7〃7:.:.:.イ　　　　　　　./ﾆ}　　　 　　 ./:::::::::::::::::::::}::::::::::::＼::::::::::::::::::＞､:.:.:.:.
　:.:.::..:.:.:.:.:.:.:.:.:.:.:.:.:.:.イ　　.r=＝/-=＝イ_x'´￣　　　　　　　　/.ﾆ{　　　　　　ﾑ:::::::::::::::::::::lミヽ::::::::::＞､::::::::::::::::::Y:.:.:.:
　:.:.:..:.:.:.:.:.:.:.:.:.:.:.,　´　　　 辷三三彡':::::::::ゝ､　　　　　　　 イニﾑ　　　　　 ハヽ::l:::::::::::::::7ヽ:.｀　､::::::::｀ー---‐ｲ:.:.:.:.
　:.:.:..:.:.:.:.:.:.:,　´　　　　　　　　　 ゝ＿＿＿_/＞‐-‐=＜´=＝=ﾆﾆゝ _＿ イ:.:.:ﾊ }::l:::::::::::::::{　ヽヽ:.:｀ー─‐----ｲ:.:.:.:.

                                    ║  [1] -> Search by Email(term@term.x)     ║by phos
                                    ║  [2] -> Search by Username               ║github.com/ph0sph0re
                                    ║  [3] -> Search by Full Name(fstname name)║put a star
                                    ║  [4] -> Search by Password               ║pls
                                    ║  [4] -> Search by hash Password          ║
                                    ║  [6] -> Search by IP Address(xx.xx.xx.xx)║
                                    ╚══════════════════════════════════════════╝
                                    ║         "Exit" = Close the script        ║
                                    ╚══════════════════════════════════════════╝
"""

SEARCH_TYPES = {
    1: "email",
    2: "username",
    3: "name",
    4: "password",
    5: "hash",
    6: "lastip"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_database(search_term, search_type):
    if not search_term:
        print("[!] Please provide a search term.")
        return

    url = 'https://api-experimental.snusbase.com/data/search'
    headers = {'Auth': API_KEY, 'Content-Type': 'application/json'}
    payload = {'terms': [search_term], 'types': [search_type], 'wildcard': False}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        results = response.json().get('results', {})
        display_search_results(results)
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

def display_search_results(results):
    if not results:
        print("\n[+] No results found.")
    else:
        for db_name, entries in results.items():
            print(f"Database: {db_name}")
            for entry in entries:
                for field, value in entry.items():
                    if field == 'lastip':
                        print(f"[+] {field}: {value} (Get Location)")
                    else:
                        print(f"[+] {field}: {value}")
                print('-' * 50)

def get_ip_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        location = response.json()
        print(f"[+] Location for {ip}: {location['city']}, {location['region']}, {location['country']}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

def main():
    clear_screen()
    print(MENU)

    while True:
        try:
            choice = input("\n[+] Select an option (or type 'exit' to quit): ")
            if choice.lower() == 'exit':
                break

            choice = int(choice)
            search_type = SEARCH_TYPES.get(choice)

            if search_type:
                search_term = input(f"[+] Enter {search_type} to search: ")
                search_database(search_term, search_type)

                if search_type == 'lastip':
                    ip = input("[+] Enter an IP to get location (or 'exit' to quit): ")
                    if ip.lower() == 'exit':
                        clear_screen()
                        break
                    get_ip_location(ip)
            else:
                print("[!] Invalid choice, please select a valid option.")

        except ValueError:
            print("[!] Please enter a valid number.")

        while True:
            continue_search = input("\n[+] Would you like to perform another search? (yes/no): ").lower()
            if continue_search == 'yes':
                clear_screen()
                print(MENU)
                break
            elif continue_search == 'no':
                break
            else:
                print("[!] Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[!] Erreur : {e}")
