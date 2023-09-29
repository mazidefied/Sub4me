import sys
import urllib.request
import urllib.parse
import re
import os

# Clear the console screen
os.system('clear')
print ("""
SUB4ME 
CODED BY GEORGE                                
""")
# Get the domain name from the user
domain = input("Enter the domain name: ").strip()

# Retrieve the subdomains for the inputted domain
domains = set()
url = f"https://crt.sh/?q=%25.{domain}"
response = urllib.request.urlopen(url)
code = response.read().decode('utf-8')
pattern = r"<td>([\w\.\-]+?\." + re.escape(domain) + r")</td>"
matches = re.findall(pattern, code, re.IGNORECASE)
for match in matches:
    domain = match.split('@')[-1]
    if domain not in domains:
        domains.add(domain)
        print(domain)

# Print the number of subdomains found
print(f"{len(domains)} subdomains found for {domain}")

# Save the subdomains to a file with the name of the domain searched
filename = f"{domain}.txt"
with open(filename, "w") as f:
    for domain in domains:
        f.write(domain + "\n")
print(f"Subdomains saved to {filename}")
