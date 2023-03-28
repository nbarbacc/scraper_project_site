import requests, json, datetime, matplotlib.pyplot as plt
import numpy as np

server_dict = {"emerald": 17, "connery": 1, "miller": 10, "cobalt": 13, "jaeger": 19, "soltech": 40}

while True:
    server_req = input("Please enter the Server you'd like to check: ").lower()

    if server_req in server_dict:
        world = server_dict[server_req]
        print(f"Checking {server_req.title()} Server:")
        break  # exit the loop if the input is valid
    else:
        print("Please enter a valid input and try again.")

print(f"Checking {server_req.title()} Server: ")

# Make a request to the API and store the response in a variable
response = requests.get(f"https://ps2.fisu.pw/api/population/?world={world}")

# Parse the response as JSON and store it in a variable
data = json.loads(response.text)

# extract timestamp and convert into standard time
cur_time = int(data["result"][0]["timestamp"])
standard_time = datetime.datetime.fromtimestamp(cur_time).strftime("%Y-%m-%d %H:%M:%S")
print(standard_time, "\n")

# Extract the integer values for vs, nc, tr, ns
vs = int(data["result"][0]["vs"])
nc = int(data["result"][0]["nc"])
tr = int(data["result"][0]["tr"])
ns = int(data["result"][0]["ns"])
total_players = vs + nc + tr + ns

sizes = [vs, nc, tr, ns]
sizes = np.nan_to_num(sizes)

labels = ['VS', 'NC', 'TR', 'NS']
colors = ['#6a0dad', '#1f77b4', '#d62728', '#7a7a7a']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title(f'{server_req.title()} Server Population by Faction')

# Get the current axis object
ax = plt.gca()
az = plt.gca()
# Add Last Updated to the center of the chart
text = f"Last updated: {standard_time}"
az.text(0.5, -1.2, text, ha='center', va='center', fontsize=8)
# Add Total Players below Last updated
text = f"Total Players: {total_players}"
ax.text(0.5, -1.3, text, ha='center', va='center', fontsize=8)
text = f"Faction Count: VS: {vs}, NC: {nc}, TR: {tr}, NS: {ns}"
ax.text(0.5, -1.4, text, ha='center', va='center', fontsize=8)

plt.show()

print(f"VS: {vs}, NC: {nc}, TR: {tr}, NS: {ns}, Total Players: {total_players}")
