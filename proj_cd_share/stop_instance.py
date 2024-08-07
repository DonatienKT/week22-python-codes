#import aws_inst_code

from aws_inst_code import listInstances,stopInstances

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

stopInstances(listInstances(dev_filter))
