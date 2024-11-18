import requests
import json
import os
import tkinter as tk
from tkinter import messagebox

def get_public_ip_info():

    api_key = os.getenv("API_KEY", "e45e222a65e81fab96f9886ebf842a7c")
    
    url = f"http://api.ipstack.com/check?access_key={api_key}"
    
    try:

        response = requests.get(url)
        
        if response.status_code == 200:

            data = response.json()
            
            ip_address = data.get('ip')
            city = data.get('city')
            region = data.get('region_name')
            country = data.get('country_name')
            country_code = data.get('country_code')
            postal = data.get('zip')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            asn = data.get('location', {}).get('geoname_id')
            isp = data.get('connection', {}).get('isp')

            ip_info = (
                f"IP Address: {ip_address}\n"
                f"City: {city}\n"
                f"Region: {region}\n"
                f"Country: {country} ({country_code})\n"
                f"Postal Code: {postal}\n"
                f"Latitude: {latitude}, Longitude: {longitude}\n"
                f"ASN (Autonomous System Number): {asn}\n"
                f"ISP: {isp}"
            )
            
            return ip_info

        else:
            return f"Failed to retrieve IP info. Status code: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"Error occurred while retrieving IP information: {e}"


def display_ip_info():
    ip_info = get_public_ip_info()
    messagebox.showinfo("Public IP Information", ip_info)

root = tk.Tk()
root.title("IP Information App")

root.geometry("400x200")

label = tk.Label(root, text="Click the button to retrieve your public IP information", wraplength=300)
label.pack(pady=20)

fetch_button = tk.Button(root, text="Get IP Info", command=display_ip_info, height=2, width=20)
fetch_button.pack(pady=10)

root.mainloop()
