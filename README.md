# RouterGhost

A wormable exploit chain on Sapido BR270n


# Reqirements

mips toolchain

https://sourcery.mentor.com/GNUToolchain/package13838/public/mips-linux-gnu/mips-2016.05-8-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2

# Usage

python main.py [router ip] [program name] ([argument1]...) 

ex:

rdir.c compile and send to 192.168.1.1 to execute rdir.c with argument /etc 


(rdir will recusively enumeration directory at /etc)

python main.py 192.168.1.1 rdir /etc

# Detail

remote 0day discovery/analysis:
http://kinmeniotfirmwaresecurity.blogspot.com/2018/12/router-ghost-possiblity-of-0day-remote.html

remote firmware/kernel hacking:

http://kinmeniotfirmwaresecurity.blogspot.com/2019/01/deep-look-at-router-0-day.html
