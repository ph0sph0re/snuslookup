import requests
import os

API_KEY = ''

MENU = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▓▓    ░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▓▓    ░░░░░░░░▒▒░░░░████▒▒████▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒  ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▓▓      ░░░░        ░░    ░░░░  ░░██░░▒▒░░░░░░░░░░    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒░░    ░░                          ░░░░░░░░          ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓▓░░▒▒                  ░░          ▒▒░░          ░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░          ░░      ░░            ░░        ░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒                    ▒▒      ░░    ░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░    ░░    ░░        ▒▒      ░░    ░░▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░  ░░  ░░    ░░▒▒▒▒  ▒▒      ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░    ░░    ▓▓        ▒▒    ░░░░    ░░      ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░    ▒▒░░  ░░▒▒▒▒░░▒▒░░      ░░      ▓▓▒▒  ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒▓▓░░  ░░▒▒▓▓████░░            ░░░░      ▒▒░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░  ░░▓▓▒▒▒▒██▒▒      ▓▓████▓▓░░░░    ▒▒▒▒    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▓▓██░░      ▒▒  ▓▓▓▓░░      ░░░░▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒    ▒▒▒▒            ▓▓▓▓  ▒▒░░░░░░  ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▓▓░░▒▒                    ░░░░  ░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒░░▒▒                        ░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓░░░░▒▒                    ░░░░░░▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒██▒▒▒▒▓▓▓▓░░    ░░    ░░░░▒▒▒▒░░▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▓▓░░▒▒▓▓▒▒▒▒▒▒▒▒░░▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒    ▒▒▓▓▒▒▒▒  ░░▒▒▒▒▒▒▓▓██▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░          ░░▓▓▓▓▓▓██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒▒▒      ▓▓░░░░        ░░  ░░▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▓▓░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒░░        ▒▒▓▓▒▒          ░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒▒▒    ▒▒░░▒▒░░      ░░▓▓▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓░░  ▓▓▒▒░░      ▒▒▒▒▒▒▓▓▒▒░░  ░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░

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
