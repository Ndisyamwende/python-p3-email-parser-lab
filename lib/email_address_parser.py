# your code goes here!
import re

class EmailAddressParser:
    '''Class for parsing email addresses'''

    def __init__(self, input_string):
        '''Constructor with a single argument, a string.'''
        self.input_string = input_string

    def parse(self):
        '''Method to parse emails from the input string.'''
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, self.input_string)
        return sorted(emails)