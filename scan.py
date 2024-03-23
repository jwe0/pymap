import socket, argparse, threading
from datetime import datetime
from tqdm import tqdm

ports = []



def check(ip, port):

    global ports


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    data = s.connect_ex((ip, port))
    if data == 0:
        ports.append(str(port))
    s.close()


def Main():

    art = """
  /\        
 /  \     ╔═╗╦ ╦╔╦╗╔═╗╔═╗
 |  |     ╠═╝╚╦╝║║║╠═╣╠═╝
 |  |     ╩   ╩ ╩ ╩╩ ╩╩
/ == \  Deved by Joshua Webb
|/**\|        /jwe0
    
    """




    print(art + "\n")
    print("[+] Started scanning @ {date}".format(date=datetime.now().strftime("%H:%M:%S")))


    parser = argparse.ArgumentParser(description="Simple python portscanner")

    parser.add_argument("--target", "-t", help="Target ip address")
    parser.add_argument("--range", "-r", help="Define the range of ports")
    
    args = parser.parse_args()


    range_start = 0
    range_end = 65535


    if args.range:

        range_start = args.range.split(",")[0]
        range_end = args.range.split(",")[1]

    with tqdm(total=int(range_end), desc="Progress") as pbar:
        for i in range(int(range_start), int(range_end)):
            threading.Thread(target=check, args=[args.target, i]).start()
            pbar.update(1)


if __name__ == "__main__":
    Main()
    print()

    for port in ports:

        print("[+] Open port enumerated succesfully: {port}".format(port=port))