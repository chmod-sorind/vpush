import telnetlib
import time

pollingRate = raw_input('Enter a poll frequency (secs).\n> ')
pollingRate = float(pollingRate) if pollingRate else float(1)

pollingCount = raw_input('Enter a poll count.\n> ')
pollingCount = int(pollingCount) if pollingCount else int(1)

with open('ip.txt') as IP:
    line = IP.read().splitlines()

for pollNum in range(1, pollingCount + 1):
    for f in line:
        try:
            telnet = telnetlib.Telnet(f, 2323)
            telnet.write("vpush\n")
            telnet.close()
            print 'Vpush#:', pollNum, f, 'Done!'
        except:
            print 'Could not connect to host:', f
    if pollNum < pollingCount:
        time.sleep(pollingRate)
print 'All Done!'