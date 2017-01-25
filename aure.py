#! /usr/bin/env python
from __future__ import print_function
import subprocess
import traceback
import sys
import time
import argparse

__version__ = '0.0.1'


def autorestart(cmd, interval):
    while True:
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            e.output
        except OSError:
            print("can't find shell command")
        except:
            traceback.print_exc()
        finally:
            time.sleep(interval)


def main():
    opt = argparse.ArgumentParser('util for auto restart shell command')
    opt.add_argument('cmd', nargs=argparse.REMAINDER, help='shell command')
    opt.add_argument('--interval', '-i', type=int, default=1, help='auto restart interval, default 1s')
    args = opt.parse_args()

    if len(args.cmd) <= 0:
        print('required shell command')
        opt.print_help()
        return
    autorestart(args.cmd, args.interval)


if __name__ == '__main__':
    main()
