import numpy as np
import sys
import math
import time
import csv
from hpolib.benchmarks.synthetic_functions import Bohachevsky # Change this
from time import gmtime, strftime

def main(job_id, params):
  print '!!! Entered Main !!!'
  print 'Anything printed here will end up in the output directory for job #:', str(job_id)
  print params
  f = Bohachevsky() # Change this
  res = f.objective_function([params['x'], params['y']]) # CHANGE THIS
  print res
  with open('/home/mansurm/Experiments/Bohachevsky/run26.csv','a') as csvfile:  # CHANGE THIS
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow([res['main'][0]])
  return res['main'][0]
