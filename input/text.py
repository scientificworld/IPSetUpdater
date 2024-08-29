import urllib.request

def run(config):
    ips = list()
    request = urllib.request.Request(config["url"], headers={"User-Agent": "Mozilla/5.0 (Python-urllib) IPSU/0.1"})
    with urllib.request.urlopen(request) as stream:
        while i := stream.readline().decode("utf-8").strip():
            if i.startswith("#"):
                continue
            ips.append(i)
    return ips
