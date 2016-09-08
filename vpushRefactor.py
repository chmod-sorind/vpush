#!"C:\Users\Sorin Diaconescu\AppData\Local\Programs\Python\Python35-32\python.exe"
import argparse


parser = argparse.ArgumentParser(description="Force a poll on BroadSign Player/Edge Server")
parser.add_argument("ip", metavar='IP', type=str, nargs='?', default="",
                    help="Target IP Address.")
parser.add_argument("--bsp", "-p", action="store_true", help="Push a poll on a BroadSign Player on port 2323 by default.")
parser.add_argument("--bses", "-e", action="store_true", help="Push a poll on a BroadSign Edge Server on port 2324 by default.")
parser.add_argument("--port", action="store_true", help="Specify a different port for telnet connection.")

args = parser.parse_args()