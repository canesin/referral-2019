#!/usr/bin/env python3
"""
Script used to generate intries list
"""
import hashlib

def is_invalid_entry_primitive(email, domains_to_exclude, emails_to_exclude):
    _, domain = email.split('@')
    top_level_domain = '.'.join(domain.split('.')[::-1][0:2][::-1])
    is_forbiden_mail = top_level_domain in domains_to_exclude
    is_forbiden_user = email in emails_to_exclude
    return is_forbiden_mail or is_forbiden_user

domains_to_exclude =['nash.io',
                     'neonexchange.org',
                     'keyrock.eu',
                     'nccgroup.trust',
                     'cure53.de',
                     'recurity-labs.com']

emails_to_exclude = open('emails_to_filter_out', 'r').read().splitlines()

is_invalid_entry = lambda email: is_invalid_entry_primitive(email, domains_to_exclude, emails_to_exclude)

participants = open('secret_list.csv', 'r').read().splitlines()

public_list = []

for person in participants:
    _, email, _, tickets = person.split(',')
    user_string = hashlib.sha256(email.encode('utf-8')).hexdigest()
    if not is_invalid_entry(email):
        public_list += int(tickets) * [user_string]

sorted_list = sorted(public_list, key = str.lower)

open('participants_nash', 'w').write("\n".join(sorted_list))