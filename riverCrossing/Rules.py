import os
import json
import pprint


class Rules:
    """
    Contains rules as object read in from file
    """

    def __init__(self, rules_file):
        self.rules_file = rules_file
        self.rules = {}        

        self.rules = self.read_json_rules()
        # output current rules
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.rules)


    def read_json_rules(self):
        with open(self.rules_file) as rules_file:
            data = json.load(rules_file)
        return data
