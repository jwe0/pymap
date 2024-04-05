import socket, argparse, threading, json
from datetime import datetime
from Utils.Colors import *

ports = []

def port_service(port):
    with open("Ports/common_ports.json") as f:
        common_ports = json.load(f)
    with open("Ports/registered_ports.json") as f:
        registered_ports = json.load(f)



    if str(port) in common_ports:
        service = common_ports[str(port)]["service"]
        protocol = common_ports[str(port)]["protocols"]

        return service, protocol

    elif str(port) in registered_ports:
        service = registered_ports[str(port)]["service"]
        protocol = registered_ports[str(port)]["protocols"]

        return service, protocol
    else:
        return "No service detected", "No protocol detected"



def check_port(socket, ip, port):
    con = socket.connect_ex((ip, port))
    if con == 0:
        serv, proto = port_service(str(port))
        print(f"[PORT]\t\t{ip}:{str(port)}\t\t{serv}\t\t{proto}")


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
    parser.add_argument("--mode", "-m,")
    
    args = parser.parse_args()




    if args.target:

        if args.mode == "ports":

            range_start = 0
            range_end = 65535

            if args.range:

                range_start = args.range.split(",")[0]
                range_end = args.range.split(",")[1]

                for i in range(int(range_start), int(range_end)):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    threading.Thread(target=check_port, args=[s, args.target, i + 1]).start()
                    print(f"[PROGRESS] ( {args.target}:{str(i + 1)} )", end='\r')


        elif args.mode == "host":
            print("[+] Host: {ip}".format(ip=socket.gethostbyname(args.target)))

    else:
        print("[+] Please supply a target")


if __name__ == "__main__":
    Main()
    print()

    for port in ports:

        print("[PORT]   >   {port}".format(port=port))
