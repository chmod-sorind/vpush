import telnetlib
import time

try:
    pollingRate = input('Enter a poll frequency (secs).\n> ')
    pollingRate = float(pollingRate) if pollingRate else float(1)
except ValueError as v:
    print("ValueError", v)
    exit()

try:
    pollingCount = input('Enter a poll count.\n> ')
    pollingCount = int(pollingCount) if pollingCount else int(1)
except ValueError as v:
    print("ValueError", v)
    exit()

with open('ip.txt') as IP:
    line = IP.read().splitlines()

for pollNum in range(1, pollingCount + 1):
    for f in line:
        try:
            if '#' not in f:
                #command = str('vpush')
                telnet = telnetlib.Telnet(f, 2323)
                telnet.write(('vpush' + '\n').encode('ascii'))
                telnet.close()
                print('Vpush#:', pollNum, f, 'Done!')
            else:
                print('Skipping', f)
        except:
            print('Could not connect to host:', f)
    if pollNum < pollingCount:
        time.sleep(pollingRate)
print('All Done!')