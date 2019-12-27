#!/usr/bin/env python3
"""
Script used to issue the winners for Nash 1st referral giveaway
"""
import hashlib

SALT_MAP = {
    1: '#15_000NEX',
    2: '#10_000NEX',
    3: '#5_000NEX',
    4: '#1_000NEX',
    5: '#500NEX_n1',
    6: '#500NEX_n2',
    7: '#500NEX_n3',
    8: '#500NEX_n4',
    9: '#500NEX_n5',
    10: '#500NEX_n6',
    11: '#500NEX_n7',
    12: '#500NEX_n8',
    13: '#500NEX_n9',
    14: '#500NEX_n10',
    15: '#500NEX_n11',
    16: '#500NEX_n12',
    17: '#500NEX_n13',
    18: '#500NEX_n14',
    19: '#500NEX_n15',
    20: '#500NEX_n16',
    21: '#500NEX_n17',
    22: '#500NEX_n18',
    23: '#500NEX_n19',
    24: '#500NEX_n20',
    25: '#500NEX_n21',
    26: '#500NEX_n22',
    27: '#500NEX_n23',
    28: '#500NEX_n24',
    29: '#500NEX_n25',
    30: '#500NEX_n26',
    31: '#500NEX_n27',
    32: '#500NEX_n28',
    33: '#500NEX_n29',
    34: '#500NEX_n30'
}

BTCHASH = '0000000000000000000f578c397736149098edce9b374eff6d90b6bc9634c05b'

participants = open('participants_nash', 'r').read().splitlines()
total_tickets = len(participants)

winners = []

for prize in SALT_MAP:
    prize_hash = hashlib.sha256((BTCHASH + SALT_MAP[prize]).encode('utf-8')).hexdigest()
    choosen_number = int(prize_hash, 16) % total_tickets
    winner = participants[choosen_number]
    winners.append(winner)
    print("| Winner for prize {} | {} |".format(prize, winner))

# This function will not run in computers without the secret_list.csv file
# only used internaly to print the winning emails
try:
    users = open('secret_list.csv', 'r').read().splitlines()
    for prize, winner in enumerate(winners):
        for user in users:
            _, email, name, _ = user.split(',')
            fist_name = name.split()[0]
            if hashlib.sha256(email.encode('utf-8')).hexdigest() == winner:
                print("| Winner for prize {} | {} | {} |".format(prize + 1, fist_name , winner))
                print("Winner for prize {}: {}, {}".format(prize + 1, email , winner))
except:
    pass