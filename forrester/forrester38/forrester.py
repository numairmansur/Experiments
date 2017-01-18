import numpy as np
import sys
import math
import time
import csv
from hpolib.benchmarks.synthetic_functions import Forrester
from time import gmtime, strftime

def main(job_id, params):
  print '!!! Entered Main !!!'
  print 'Anything printed here will end up in the output directory for job #:', str(job_id)
  print params
  f = Forrester()
  res = f.objective_function([params['x']])
  print res
  #with open('/home/numair/Downloads/testEnvFortheCluster/Experiments/forrester/run1.csv','a') as csvfile:
  with open('/home/mansurm/Experiments/forrester/run38.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow([res['main'][0]])
  return res['main'][0]