# Pymap

```
  /\
 /  \     ╔═╗╦ ╦╔╦╗╔═╗╔═╗
 |  |     ╠═╝╚╦╝║║║╠═╣╠═╝
 |  |     ╩   ╩ ╩ ╩╩ ╩╩
/ == \  Deved by Joshua Webb
|/**\|        /jwe0
```

Pymap is a python version of the popular nmap utility which can be found @ `http://nmap.org`.\
Pymap has significantly less features compared to nmap so if you need to scan a web application properly use nmap.\
Pymap takes 42 seconds to scan 65535 ports with 8GB of ddr3, an Intel i3-2120 at 3.30GHz and an NVIDIA GeForce GT 710

# Install
1. Run `git clone https://jwe0/pymap` to clone the repository
2. Run `cd pymap` to change your location to the active directory
3. Finally run `python scan.py -h` for mage help.
4. Enjoy :)


# Examples
```shell
~ Port mode ~

python scan.py -m ports -t 127.0.0.1 -r 0,8080
python scan.py --mode ports --target 127.0.0.1 --range 0,8080

~ Enum mode ~

python scan.py -m host -t google.com
python scan.py --mode host --target google.com
```

# Regards
I take no legal responsiblity for any negative actions commited with my software. This was made for ethical purposes only <3.
