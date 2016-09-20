import argparse
import telnetlib
import time
import sys


PORT_NUMBER = (2322, 2323)
TARGET_HOST_IP = []

parser = argparse.ArgumentParser(description='Send a command via telnet connection to BroadSign Player/Edge Server.')
parser.add_argument('command', metavar='COMMAND', type=str, nargs='?', default='vpush', help='Command you want to send to the target IP via telnet connection. Default command is notorious vpush.')
parser.add_argument('--bsp',  action='store_true', help='Push a poll on a BroadSign Player on port 2323 by default.')
parser.add_argument('--bses', action='store_true', help='Push a poll on a BroadSign Edge Server on port 2324 by default.')
parser.add_argument('--port', '-p', action='store', type=int, help="Specify a different port for the telnet connection (default: bsp[{1}], bses[{0}]).".format(PORT_NUMBER[0], PORT_NUMBER[1]))

parser.add_argument('--ip', '-t', nargs='+', help='Specify one target IP or a list of IPs in a comma separated list.')

#parser.add_argument('--ip', '-t', nargs='?', help='Specify one target IP or a list of IPs in a comma separated list.')
parser.add_argument('--file', '-f', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Specify a file that contains a list of IPs (one IP per row).')
parser.add_argument('--frequency', '-fq', type=str, nargs=1, default=1,help='Specify the frequency of the poll in seconds. Default value is 30.')
parser.add_argument('--count', '-c', nargs=1, default=1, help='Specify the number of repetitions. Default value is 1.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if __name__ == '__main__':

    if args.port is None:
        if args.bses is True:
            args.port = PORT_NUMBER[0]
        elif args.bsp is True:
            args.port = PORT_NUMBER[1]
        elif args.port is None and args.bsp is False and args.bses is False:
            args.port = PORT_NUMBER[1]
            print("Default bsp[{1}] port will be used since no other option was specified.".format(PORT_NUMBER[0], PORT_NUMBER[1]))

    print(args.ip)
    print(args.file)

    print(args)


''' some tests.
Will be removed when I'm done.
#print('port type is: ', type(args.port))
#pollFreq = args.frequency
#pollFreq = map(float, pollFreq)
#print(type(pollFreq))
#print(pollFreq)


#def setFreqAndCount(pollFreq, pollCount):
#    pollFreq = args.frequency
#    pollCount = args.count
END some tests '''