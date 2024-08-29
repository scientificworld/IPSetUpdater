import urllib.request
import ssl

def run(config, ips):
    context = ssl.create_default_context()
    if "allow_insecure" in config:
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    api_token = config["user"] + "!" + config["token"]
    for i in ips:
        print(i)
        request = urllib.request.Request(f"https://{config["host"]}/api2/json/nodes/{config["node"]}/{config["type"]}/{config["vmid"]}/firewall/ipset/{config["name"]}", data=f"cidr={str(i)}".encode(), headers={"Authorization": f"PVEAPIToken={api_token}"}, method="POST")
        try:
            urllib.request.urlopen(request, context=context)
        except:
            pass
