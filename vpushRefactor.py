import argparse
import telnetlib
import time
import sys

PORT_NUMBER_LIST = (2322, 2323)
TARGET_HOST_IP = []
TARGET_HOST_PORT = ''
POLLING_COUNT = ''
POLLING_RATE = ''
VERSION = "0.2.0"

'''
V 0.2.0
Store the correct argument type for each option.
Resolve conflicts when setting the TARGET_HOST_PORT port.
Changed the way the argument for input files is set.
Added a check for --file/-f.
'''

parser = argparse.ArgumentParser(description='Send a command via telnet connection to BroadSign Player/Edge Server.')
parser.add_argument('command', metavar='COMMAND', type=str, nargs='?', default='vpush', help='Command you want to send to the target IP via telnet connection. Default command is notorious vpush.')
parser.add_argument('--bsp', action='store_true', help='Push a poll on a BroadSign Player on port 2323 by default.')
parser.add_argument('--bses', action='store_true', help='Push a poll on a BroadSign Edge Server on port 2324 by default.')
parser.add_argument('--port', '-p', action='store', type=int, help="Specify a different port for the telnet connection (default: bsp[{1}], bses[{0}]).".format(PORT_NUMBER_LIST[0], PORT_NUMBER_LIST[1]))
parser.add_argument('--ip', '-t', nargs='+', help='Specify one target IP or a list of IPs.')
parser.add_argument('--file', '-f', action='store', type=argparse.FileType('r'), help='Specify a file that contains a list of IPs (one IP per row).')  # type=argparse.FileType('r'), default=sys.stdin
parser.add_argument('--frequency', '-fq', default=30, type=float, help='Specify the frequency of the poll in seconds. Default value is 60.')
parser.add_argument('--count', '-c', default=1, type=int, help='Specify the number of repetitions. Default value is 1.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + VERSION)
args = parser.parse_args()

if __name__ == '__main__':

    def query_yes_no(question, default="port"):
        valid = {"yes": True, "y": True, "ye": True, "port": True, "por": True, "po": True, "p": True,
                 "no": False, "n": False, "bsp": False, "bses": False, "bse": False, "bs": False, "b": False}
        if default is None:
            print("Sorry need an answer...")
            prompt = " [port/bsp/bses] "
        elif default == "port":
            prompt = " [port/bsp/bses] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)
        while True:
            sys.stdout.write(question + prompt)
            choice = input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

    # First check if  all the necessary options were passed to the script or passed multiple times.

    if args.file is None and args.ip is None:
        print("Please select at least one option for target ip (--ip/-t [IP] OR --file/-f [FILE])")
        quit(print("Script failed.."))

    if args.file is not None and args.ip is not None:
        print("Oops... You specified too many options for the target ip ( --ip AND --file).\n"
              "Please select only one option for target ip (--ip/-t [IP] OR --file/-f [FILE])")
        quit(print("Script failed..."))

    if args.ip is not None:
        for ip in args.ip:
            TARGET_HOST_IP.append(ip)
    elif args.file is not None:
        for ip in args.file.readlines():
            line_ip = ip.rstrip()
            TARGET_HOST_IP.append(line_ip)

    if args.port is None and args.bsp is False and args.bses is False:
        print("Please select at least one option for target port (--port/-p [PORT] OR --bsp OR --bses)")
        quit(print("Script failed..."))

    if args.bsp is True and args.bses is True:
        print("Oops.. You specified too many options for the destination port (--bsp AND --bses).\n"
              "Please select only one option for target port (--bsp OR --bses)")
        quit(print("Script failed..."))

    if args.port is not None and args.bsp is True and args.bses is True:
        print("You specified way too many options for the destination port (--port/-p AND --bsp AND --bses).\n"
              "Please select only one option for target port (--port/-p [PORT] OR --bsp OR --bses)")
        quit(print("Script will now exit."))

    if args.port is not None and args.bsp is True:
        answer_BSP = query_yes_no\
            ("You specified too many options for the destination port (--port/-p AND --bsp).\n"
             "Type port to continue with the value set by --port/-p option:[{0}].\n"
             "Type bsp continue with the default value for bsp[2323].".format(args.port))
        if answer_BSP is False:
            TARGET_HOST_PORT = PORT_NUMBER_LIST[1]
        else:
            TARGET_HOST_PORT = args.port
    elif args.port is not None and args.bses is True:
        answer_BSES = query_yes_no\
            ("You specified too many options for the destination port (--port/-p AND --bses).\n"
             "Type port to continue with the value set by --port/-p option:[{0}].\n"
             "Type bses to continue with default value for bses[2322].".format(args.port))
        if answer_BSES is False:
            TARGET_HOST_PORT = PORT_NUMBER_LIST[0]
        else:
            TARGET_HOST_PORT = args.port
    elif args.port is not None:
        TARGET_HOST_PORT = args.port
    elif args.bsp is True:
        TARGET_HOST_PORT = PORT_NUMBER_LIST[1]
    elif args.bses is True:
        TARGET_HOST_PORT = PORT_NUMBER_LIST[0]

    print('target port number is: ', TARGET_HOST_PORT)
    print('ip value: ', TARGET_HOST_IP)
    print('file value: ', args.file)
    print('count value: ', args.count)
    print('frequency value: ', args.frequency)
    print('command value: ', COMMAND)


    def do_telnet(TARGET_HOST_IP, TARGET_HOST_PORT, POLLING_COUNT, POLLING_RATE, COMMAND):

        return
