import argparse
import telnetlib
import time


parser = argparse.ArgumentParser(description='Send a command via telnet connection to BroadSign Player/Edge Server.')
parser.add_argument('command', metavar='COMMAND', type=str, nargs='?', default='vpush',
                    help='Command you want to send to the target IP via telnet connection. Default command is notorious'
                         ' vpush.')
parser.add_argument('--bsp',  action='store_const', const=2323, help='Push a poll on a BroadSign Player on port 2323 by'
                                                                     ' default.')
parser.add_argument('--bses', action='store_const', const=2324, help='Push a poll on a BroadSign Edge Server on port'
                                                                     ' 2324 by default.')
parser.add_argument('--port', '-p', action='store_true', help='Specify a different port for the telnet connection.')
parser.add_argument('--ip', '-t', action='store_true', help='Specify one target IP or a list of IPs in a comma separated'
                                                            ' list.')
parser.add_argument('--file', '-f', action='store_true', help='Specify a file that contains a list of IPs (one IP per'
                                                              'row).')
parser.add_argument('--frequency', '-fq', action='store_true', help='Specify the frequency of the poll in seconds.'
                                                                    ' Default value is 30.')
parser.add_argument('--count', '-c', action='store_true', help='Specify the number of repetitions. Default value is 1.')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()