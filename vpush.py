import telnetlib
import time

# Define the list of hosts.
listIP = 'ip.txt'

# Set freq from input and change the var type from str to float.
freqInput = raw_input('Enter a poll frequency (secs): ')
freq = float(freqInput)

# Set pollCount from input and change the var type from str to int.
pollCountInput = raw_input('Enter a poll count: ')
pollCount = int(pollCountInput)

# Read the list of hosts and split the lines.
with open(listIP) as IP:
    line = IP.read().splitlines()

i = 0  # Set the while count to 0.
while i < pollCount:
    for f in line:
        telnet = telnetlib.Telnet(f, 2323)  # Establish telnet connection to host.
        telnet.write("vpush\n")  # Send command to host.
        print telnet.read_all()  # Read all data until EOF; block until connection closed.
        telnet.close()  # Disconnect telnet.
        print i, 'Vpush', f, 'Done!'  # Print Feedback.
    i += 1  # Increment while count.
    if i == pollCount:  # If i is equal to pollCount quit the script before last sleep.
        print 'All Done!\nQuitting... '
        quit()
    time.sleep(freq)  # Apply the frequency of poll.
