#!/usr/bin/env python3
import sys
import requests
import re
import json
from datetime import datetime
from dateutil import tz

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

  from_zone = tz.tzutc()
  to_zone = tz.tzlocal()

  for c in data:
    date_str = c["commit"]["committer"]["date"]

    utc = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    utc = utc.replace(tzinfo=from_zone)

    local_tz = utc.astimezone(to_zone)

    c_time = local_tz.strftime('%Y-%m-%d %H:%M:%S %Z')

    print()
    print("Created %s" % c_time)
    print("Commit SHA: %s" % c["sha"])
    print("Commit URL: %s" % c["html_url"])
    print("Committer: %s" % c["commit"]["committer"]["name"])
    print()
    print(c["commit"]["message"])
    print()
    print('--------------------------------------------------')

  return 0

if __name__ == "__main__":
  e = main()
  exit(e)

