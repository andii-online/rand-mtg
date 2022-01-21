#!/usr/bin/env python
import argparse
import json
import random

parser = argparse.ArgumentParser(description='Generate random mtg card names...')
parser.add_argument('n', type=int, help='the number of cards to generate.')
parser.add_argument('--out', nargs='?', const=1, default='out.txt', type=str,
                    help='the file to send this mtg cardnames to')
args = parser.parse_args()

print(f'Generating {args.n} and sending it to {args.out}.')

# Load the full set of magic cards
f = open('mtg.json')
mtg_full_set = json.load(f)
f.close()

# Clean out tokens
for card in mtg_full_set:
    if 'Token' in card['type_line'] or 'Card' in card['type_line'] or 'Plane' in card['type_line'] or 'Vanguard' in card['type_line']:
        mtg_full_set.remove(card)

# Choose N cards at random
rand_mtg_set = random.choices(mtg_full_set, k=args.n)

# save file at location specified
out = open(args.out, 'w+')

for card in rand_mtg_set:
    name = card['name'].split(' //')
    out.write(name[0] +'\n')

out.close()

