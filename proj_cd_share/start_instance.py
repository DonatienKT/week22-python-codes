#import aws_inst_code

from aws_inst_code import listInstances,startInstances

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

insts = listInstances(dev_filter)
startInstances(insts)