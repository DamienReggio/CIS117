##
# Program Header:
# CIS 117 Python Programming: Lab #9
# Name: Damien Reggio
# Description: internet
# Application: www and re
# Development Environment: Windows 7/Ubuntu 14.04
# Version: Python 3.7
# Filename: DamienReggioLab8.py
# Date: 4/09/2020

import re, urllib.request, datetime

# NAS search terms
#
TERMS = ['research', 'climate', 'evolution', 'cultural', 'leadership',
         'COVID-19', 'technology']
URL = 'http://www.nasonline.org'

def main():

    nas_site = urllib.request.urlopen(URL)
    #
    #validate site

    nas_html = nas_site.read()
    # Convert from bytes
    #
    nas_html =  nas_html.decode('utf-8')
    # validate decode
    #

    print('todays date is', datetime.date.today())

    # Strip out HTML comments (they wont show up on the page)
    #
    nas_html_clean = re.sub('<!--(.*?)-->', '', nas_html,
                            count=0, flags=re.DOTALL)

    for term in TERMS:
        # make sure work is between HTML code
        # and NOT contained in another word (will be running case insensitive)
        #
        match_string = '>[^<]*' + '\\b' + term + '\\b' + '[^>]*<'
        matches = re.findall(match_string, nas_html_clean,
                             flags= re.IGNORECASE | re.DOTALL)
        num_occurences = len(matches)
        print('{} occured {} times'.format(term, num_occurences))


if __name__ == '__main__':
    main()


# output
#
'''

'''
