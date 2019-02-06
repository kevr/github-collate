#!/usr/bin/env python3
import sys
import requests
import re
import json

def usage():
  print("usage: %s 'user/repo'" % sys.argv[0])
  return 1

def main():
  if len(sys.argv) == 1 or sys.argv[1].count('/') != 1:
    return usage()

  response = requests.get('https://api.github.com/repos/%s/commits' % sys.argv[1])
  if response.status_code == 404:
    print("That repository does not exist on github.")
    return 2
  elif response.status_code != 200:
    print("Github API returned status %d." % response.status_code)
    return 3

  content = response.content.decode('UTF-8')
  data = json.loads(content)
  print(data)

  return 0

if __name__ == "__main__":
  e = main()
  exit(e)

