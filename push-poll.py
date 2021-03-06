import argparse
import telnetlib
import sys
import requests

PORT_LIST = (2322, 2323)
TARGET_HOST_IP = []
VERSION = "0.2.3"


# ToDo Make vpush a variable called command that can be changed. push or vpush could be used.
# ToDo Clean-up unnecessary script arguments
# ToDO Implement *args and *kwargs


class Host:
    id = 0

    def __init__(self, p):
        self.p = p
        self.id += 1

    def __del__(self):
        self.id -= 1

    @staticmethod
    def get_ip_list_len(ip_list):
        """Returns the length of a list containing all the target hosts"""
        return len(ip_list)

    @staticmethod
    def get_ip(ip_list, position):
        return ip_list[position]

    # Is this even necessary
    @staticmethod
    def set_port(p='2323'):
        return p

    def push(self, ip):
        try:
            telnet = telnetlib.Telnet(ip, self.p, timeout=3)
            telnet.write('vpush\n'.encode('UTF-8'))
            telnet.close()
            print("Command sent to Host: {}:{}".format(ip, self.p))
        except Exception as telnetError:
            print("Host: {0} {1}".format(ip, telnetError))


def print_warning_msg(warning_msg, default=""):
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
        sys.stdout.write(warning_msg + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            print("\nSorry you need to select one option... Invalid choice for: '%s'" % default)
        elif choice not in valid:
            print("Not a valid option.")
        elif choice in valid:
            return choice


def get_target_host_ip(ip, file):  # Do a check on ip/file options and make the user picks only one.
    if file is None and ip is None:
        print("Please select at least one option for target ip (--ip/-t [IP] OR --file/-f [FILE])")
        quit(print("Script failed.."))
    elif file is not None and ip is not None:
        warning_msg_ip = print_warning_msg("You specified too many options for the target ip ( --ip AND --file).\n"
                               "Type file to continue targeting hosts specified in file[{0}].\n"
                               "Type ip to continue targeting hosts specified list by --ip/-t {1}".
                                      format(file.name, ip), default="ip/file")
        if warning_msg_ip == "ip":
            for i in ip:
                TARGET_HOST_IP.append(i)
        elif warning_msg_ip == "file":
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


def get_target_host_port(port, bsp, bses):  # Do a check on port/bsp/bses options and make the user pick only one.
    if port is None and bsp is False and bses is False:
        print("Please select at least one option for target port (--port/-p [PORT] OR --bsp OR --bses)")
        quit(print("Script failed..."))
    elif bsp is True and bses is True:
        answer_bsp_bses = print_warning_msg \
            ("\nYou specified too many options for the destination port (--bsp AND --bses).\n"
             "Type bsp to continue with the value set by --bsp[2323]"
             "Type bses to continue with the value set by --bses[2322]", default="bsp/bses")
        if answer_bsp_bses == "bsp":
            target_host_port = PORT_LIST[1]
        elif answer_bsp_bses == "bses":
            target_host_port = PORT_LIST[0]
    elif port is not None and bsp is True and bses is True:
        print("\nYou specified way too many options for the destination port (--port/-p AND --bsp AND --bses).\n"
              "Please select only one option for target port (--port/-p [PORT] OR --bsp OR --bses)")
        quit(print("Script will now exit."))
    elif port is not None and bsp is True:
        answer_port_bsp = print_warning_msg \
            ("\nYou specified too many options for the destination port (--port/-p AND --bsp).\n"
             "Type port to continue with the value set by --port/-p option:[{0}]. OR Type bsp to continue with the default value for bsp[2323].".
             format(port), default="port/bsp")
        if answer_port_bsp == "bsp":
            target_host_port = PORT_LIST[1]
        elif answer_port_bsp == "port":
            target_host_port = port
    elif port is not None and bses is True:
        answer_port_bses = print_warning_msg \
            ("\nYou specified too many options for the destination port (--port/-p AND --bses).\n"
             "Type port to continue with the value set by --port/-p option:[{0}].\n"
             "Type bses to continue with default value for bses[2322].".
             format(port), default="port/bses")
        if answer_port_bses == "bses":
            target_host_port = PORT_LIST[0]
        elif answer_port_bses == "port":
            target_host_port = port
    elif port is not None:
        target_host_port = port
    elif bsp is True:
        target_host_port = PORT_LIST[1]
    elif bses is True:
        target_host_port = PORT_LIST[0]
    return target_host_port  # Not sure how to fix this Message: "Local Variable (#) might be referenced before assignment.".


def get_frequency(frequency):
    return frequency


def get_count(count):
    return count


## DEPRECATED for now maybe use this later to determine weter is a regular or a forced poll
# def get_command(command):
#     return command
## DEPRECATED.
# def run_telnet_connection(hosts, port, poll_rate, poll_count, command):
#     for pollNum in range(1, poll_count + 1):
#         for ip in hosts:
#             try:
#                 if '#' not in ip:
#                     telnet = telnetlib.Telnet(ip, port, timeout=3)
#                     telnet.write((command + '\n').encode('UTF-8'))
#                     telnet.close()
#                     print("#{0} Command {1} sent to {2}".format(pollNum, command, ip))
#                 else:
#                     print('Skipping connection to: {}'.format(ip))
#             except Exception as e:
#                 print("#{} ".format(pollNum), e, "Host: {}".format(ip))
#                 # print("Could not connect to host: {}".format(ip))
#         if pollNum < poll_count:
#             pollrate = int(poll_rate)
#             print("Sleeping for {} seconds".format(pollrate))
#             while pollrate > 0:
#                 minutes, sec = divmod(pollrate, 60)
#                 countdown = '{:02d}:{:02d}'.format(minutes, sec)
#                 print(countdown, end='\r')
#                 time.sleep(1)
#                 pollrate -= 1
#     return 0




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send a command via telnet connection to BroadSign Player/Edge Server.')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + VERSION)
    parser.add_argument('--bsp', action='store_true', help='Push a poll on a BroadSign Player on port 2323 by default.')
    parser.add_argument('--bses', action='store_true', help='Push a poll on a BroadSign Edge Server on port 2324 by default.')
    parser.add_argument('--port', '-p', action='store', type=int, help="Specify a different port for the telnet connection (default: bsp[{1}], bses[{0}]).".format(PORT_LIST[0], PORT_LIST[1]))
    parser.add_argument('--ip', '-t', nargs='+', help='Specify one target IP or a list of IPs.')
    parser.add_argument('--file', action='store', type=argparse.FileType('r'), help='Specify a file that contains a list of IPs (one IP per row).')
    parser.add_argument('--frequency', '-f', default=1, type=float, help='Specify the frequency of the poll in seconds. Default value is 1 sec.')
    parser.add_argument('--count', '-c', default=1, type=int, help='Specify the number of repetitions. Default value is 1.')
    args = parser.parse_args()

    try:
        port = get_target_host_port(args.port, args.bsp, args.bses)
    except Exception as e:
        print(e)

    try:
        for i in get_target_host_ip(args.ip, args.file):
            player = Host(port)
            player.push(i)
    except KeyboardInterrupt:
        print("process interrupted by user...")

