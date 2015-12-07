import telnetlib  # The telnetlib module provides a Telnet class that implements the Telnet protocol.
import time  # Time module provides various time-related functions.

# Get the polling interval from user input.
pollingRate = raw_input('Enter a poll frequency (secs).\n> ')
# Change var type from string to float as raw_input is a string type var and pollingRate, which will be used as time var
# should be a float type var.
# Set it to 1 as 'default' if there is no input from user.
pollingRate = float(pollingRate) if pollingRate else float(1)

# Get polling count from user input.
pollingCount = raw_input('Enter a poll count.\n> ')
# Change var type from string to int as raw_input is a string type var and pollingCount, which will be used in for loop
# should be a integer type var.
# Set it to 1 as 'default' if there is no input from user.
pollingCount = int(pollingCount) if pollingCount else int(1)

# Opening files using "with" statement will automatically close the file after the nested block of code is executed.
with open('ip.txt') as IP:
    line = IP.read().splitlines()  # The method splitlines() returns a list with all the lines in string

# Open a telnet connection for each host in the list.
for pollNum in range(1, pollingCount + 1):
    for f in line:
        try:  # Catch any connection error.
            telnet = telnetlib.Telnet(f, 2323)  # Establish telnet connection to host.
            telnet.write("vpush\n")  # Send command to host.
            telnet.close()  # Close Telnet connection.
            print 'Vpush#:', pollNum, f, 'Done!'  # Print feedback per host.
        except:
            print 'Could not connect to host:', f  # Print exception if any.
    if pollNum < pollingCount:
        time.sleep(pollingRate)  # Skipp the sleep time if the poll count has been reached.
print 'All Done!'  # Print feedback at the end of script.
