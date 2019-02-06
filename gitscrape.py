#!/usr/bin/env python3
import sys
import requests
import re

def usage():
  print("usage: %s 'user/repo'" % sys.argv[0])
  return 1

def main():
  if len(sys.argv) == 1 or sys.argv[1].count('/') != 1:
    return usage()

  return 0

if __name__ == "__main__":
  e = main()
  exit(e)

