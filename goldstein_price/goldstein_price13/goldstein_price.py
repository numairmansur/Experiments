import numpy as np
import sys
import math
import time
import csv
from hpolib.benchmarks.synthetic_functions import GoldsteinPrice
from time import gmtime, strftime

def main(job_id, params):
  print '!!! Entered Main !!!'
  print 'Anything printed here will end up in the output directory for job #:', str(job_id)
  print params
  f = GoldsteinPrice()
  res = f.objective_function([params['x'], params['y']])
  print res
  with open('/home/mansurm/Experiments/goldstein_price/run13.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow([res['main'][0]])
  return res['main'][0]
