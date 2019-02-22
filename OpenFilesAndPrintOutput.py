import re
import os
import csv

path = '/Users/wesleythijs/xg-argenta-mobile-testing/test-API/src/test/resources/tests'
regexScen = re.compile('Scenario:(.*?\\n)')
regexScenOutline = re.compile('Scenario Outline:(.*?\\n)')
NewLineString = '\r\n'

with open('output.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            file = open(root + "/" + filename, 'r')
            print("Module:\t" + filename)
            for line in file.readlines():
                methodNames = re.findall(regexScen, line)
                for method in methodNames:
                    if method is not None:
                        print("\t\tTest:\t" + method)
                        spamwriter.writerow([filename,method.strip()])

                methodNamesOutlines = re.findall(regexScenOutline, line)
                for method in methodNamesOutlines:
                    if method is not None:
                        print("\t\tTest outline:\t" + method)
                        spamwriter.writerow([filename, method.strip()])