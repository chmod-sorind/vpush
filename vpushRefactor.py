import argparse
import telnetlib
import time
import sys

PORT_NUMBER_LIST = (2322, 2323)
TARGET_HOST_IP = []
TARGET_HOST_PORT = ''
POLLING_COUNT = ''
POLLING_RATE = ''
VERSION = "0.2.1"

# ToDo: Build target_host_port function to return TARGET_HOST_PORT. It should take 3 arguments (port, bsp, bses) which will use args.port, args.bsp and args.bses.
# ToDo: Build frequency function to return FREQUENCY. It should take 2 arguments (frequency, default) which will use args.frequency.
# ToDo: Build count function to return COUNT. It should take 2 arguments (frequency, default) which will use args.count.
# ToDo: Build the do_telnet function. It should take 5 arguments (TARGET_HOST_IP, TARGET_HOST_PORT, POLLING_COUNT, POLLING_RATE, COMMAND) which will use the returns from all the other functions.
# ToDo: Remove or comment-out all lines with # Control Line.


'''
V 0.2.0
Store the correct argument type for each option.
Resolve conflicts when setting the TARGET_HOST_PORT port.
Changed the way the argument for input files is set.
Added a check for --file/-f.

V 0.2.1
Added a couple of ToDo points.
Build the function get_answer to resolve conflicts between arguments.
Build the function get_target_host_ip to get the target ip/ips from option --file/-f OR --ip/-t. Returns TARGET_HOST_IP.
'''

parser = argparse.ArgumentParser(description='Send a command via telnet connection to BroadSign Player/Edge Server.')
parser.add_argument('command', metavar='COMMAND', type=str, nargs='?', default='vpush', help='Command you want to send to the target IP via telnet connection. Default command is notorious vpush.')
parser.add_argument('--bsp', action='store_true', help='Push a poll on a BroadSign Player on port 2323 by default.')
parser.add_argument('--bses', action='store_true', help='Push a poll on a BroadSign Edge Server on port 2324 by default.')
parser.add_argument('--port', '-p', action='store', type=int, help="Specify a different port for the telnet connection (default: bsp[{1}], bses[{0}]).".format(PORT_NUMBER_LIST[0], PORT_NUMBER_LIST[1]))
parser.add_argument('--ip', '-t', nargs='+', help='Specify one target IP or a list of IPs.')
parser.add_argument('--file', '-f', action='store', type=argparse.FileType('r'), help='Specify a file that contains a list of IPs (one IP per row).')
parser.add_argument('--frequency', '-fq', default=30, type=float, help='Specify the frequency of the poll in seconds. Default value is 60.')
parser.add_argument('--count', '-c', default=1, type=int, help='Specify the number of repetitions. Default value is 1.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + VERSION)
args = parser.parse_args()

if __name__ == '__main__':

    def get_answer(question, default=""):
        valid = {"port", "bsp", "bses", "file", "ip"}
        if default == "port/bsp":
            prompt = " [port/bsp] "
        elif default == "port/bses":
            prompt = " [port/bses] "
        elif default == "bsp/bses":
            prompt = " [bsp/bses] "
        elif default == "ip/file":
            prompt = " [file/ip] "
        while True:
            sys.stdout.write(question + prompt)
            choice = input().lower()
            if default is not None and choice == '':
                print("\nSorry need an answer... Invalid answer for: '%s'" % default)
            elif choice in valid:
                return choice

    # First check if  all the necessary options were passed to the script or passed multiple times.

    def get_target_host_ip(ip, file):  # Do a check on ip/file options and make the user pick only one.
        if file is None and ip is None:
            print("Please select at least one option for target ip (--ip/-t [IP] OR --file/-f [FILE])")
            quit(print("Script failed.."))
        elif file is not None and ip is not None:
            answer_ip = get_answer\
                ("You specified too many options for the target ip ( --ip AND --file).\n"
                 "Type file to continue targeting hosts specified in file[{0}].\n"
                 "Type ip to continue targeting hosts specified list by --ip/-t {1}".
                 format(file.name, ip), default="ip/file")
            if answer_ip == "ip":
                for i in ip:
                    TARGET_HOST_IP.append(i)
            elif answer_ip == "file":
                for i in file.readlines():
                    line_ip = i.rstrip()
                    TARGET_HOST_IP.append(line_ip)
        elif ip is not None:
            for i in ip:
                TARGET_HOST_IP.append(i)
        elif file is not None:
            for i in file.readlines():
                line_ip = i.rstrip()
                TARGET_HOST_IP.append(line_ip)
        return TARGET_HOST_IP

    a = get_target_host_ip(args.ip, args.file)  # Control Line
    print(a)  # Control Line

    # Do a check on port/bsp/bses options and make the user pick only one.
    if args.port is None and args.bsp is False and args.bses is False:
        print("Please select at least one option for target port (--port/-p [PORT] OR --bsp OR --bses)")
        quit(print("Script failed..."))
    elif args.bsp is True and args.bses is True:
        ANSWER_BSP_BSES = get_answer\
            ("You specified too many options for the destination port (--bsp AND --bses).\n"
             "Type bsp to continue with the value set by --bsp[2323]"
             "Type bses to continue with the value set by --bses[2322]", default="bsp/bses")
        if ANSWER_BSP_BSES == "bsp":
            TARGET_HOST_PORT = PORT_NUMBER_LIST[1]
        elif ANSWER_BSP_BSES == "bses":
            TARGET_HOST_PORT = PORT_NUMBER_LIST[0]
    elif args.port is not None and args.bsp is True and args.bses is True:
        print("You specified way too many options for the destination port (--port/-p AND --bsp AND --bses).\n"
              "Please select only one option for target port (--port/-p [PORT] OR --bsp OR --bses)")
        quit(print("Script will now exit."))
    elif args.port is not None and args.bsp is True:
        ANSWER_PORT_BSP = get_answer\
            ("You specified too many options for the destination port (--port/-p AND --bsp).\n"
             "Type port to continue with the value set by --port/-p option:[{0}].\n"
             "Type bsp to continue with the default value for bsp[2323].".
             format(args.port), default="port/bsp")
        if ANSWER_PORT_BSP == "bsp":
            TARGET_HOST_PORT = PORT_NUMBER_LIST[1]
        elif ANSWER_PORT_BSP == "port":
            TARGET_HOST_PORT = args.port
    elif args.port is not None and args.bses is True:
        ANSWER_PORT_BSES = get_answer\
            ("You specified too many options for the destination port (--port/-p AND --bses).\n"
             "Type port to continue with the value set by --port/-p option:[{0}].\n"
             "Type bses to continue with default value for bses[2322].".
             format(args.port), default="port/bses")
        if ANSWER_PORT_BSES == "bses":
            TARGET_HOST_PORT = PORT_NUMBER_LIST[0]
        elif ANSWER_PORT_BSES == "port":
            TARGET_HOST_PORT = args.port
    elif args.port is not None:
        TARGET_HOST_PORT = args.port
    elif args.bsp is True:
        TARGET_HOST_PORT = PORT_NUMBER_LIST[1]
    elif args.bses is True:
        TARGET_HOST_PORT = PORT_NUMBER_LIST[0]

    print('target port number is: ', TARGET_HOST_PORT)  # Control Line
    print('ip value: ', TARGET_HOST_IP)  # Control Line
    if args.file is not None:
        print('file value: ', args.file.name)  # Control Line
    print('count value: ', args.count)  # Control Line
    print('frequency value: ', args.frequency)  # Control Line
    print('command value: ', "COMMAND")  # Control Line


    def do_telnet(TARGET_HOST_IP, TARGET_HOST_PORT, POLLING_COUNT, POLLING_RATE, COMMAND):

        return
