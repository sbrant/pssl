#!/usr/bin/python
#
# -----------------------------------------------
# Example of a Q&D script to grab the latest ja3 lookup and 
# write it out as a csv, suitable to be used as a Splunk lookup.
#
# Written by Steve Brant
# -----------------------------------------------

import json
import csv
import urllib

src_url = 'https://raw.githubusercontent.com/trisulnsm/trisul-scripts/master/lua/frontend_scripts/reassembly/ja3/prints/ja3fingerprint.json'
local_file = '/tmp/ja3_prints.json'
processed_file = '/tmp/ja3_lookup.csv'

def fetch_list():
    urllib.urlretrieve(src_url, local_file)

def prep_lookup():
    with open(local_file, 'r') as json_file:
        processedfile = open(processed_file, 'w')
        processedfile.write('ja3,ja3_desc\n')
        for row in json_file:
            if '{' not in row:
                continue
            else:
                ja3_dict = json.loads(row)
                processedfile.write(ja3_dict['ja3_hash'] + ',' + ja3_dict['desc'] + '\n')
    processedfile.close()

def main():
    fetch_list()
    prep_lookup()

if __name__ == "__main__":
    main()
