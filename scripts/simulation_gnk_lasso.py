from experiment_utils import run_model_across_sample_sizes
from utils import *
import argparse
import pickle
from datetime import datetime
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('model_name', type=str)
parser.add_argument('L', type=int)
parser.add_argument('q', type=int)
parser.add_argument('Vstr', type=str)
parser.add_argument('K', type=int)
parser.add_argument('max_num_samples', type=int)
parser.add_argument('num_samples_step', type=int)
parser.add_argument('num_replicates', type=int, nargs='?', default=1)
args = parser.parse_args()
start_time = datetime.now()

with open('data/gnk_L{}_q{}_V{}_K{}.pkl'.format(args.L, args.q, args.Vstr, args.K), 'rb') as f:
	gnk_model = pickle.load(f)

X = gnk_model['X']
y = gnk_model['y']
beta = gnk_model['beta']
num_samples_arr = np.arange(100, args.max_num_samples, args.num_samples_step)
groups = get_group_assignments(L=args.L, q=args.q)

results = run_model_across_sample_sizes(X, y, 
	beta=beta, 
	model_name=args.model_name,
	num_samples_arr=num_samples_arr,
	num_replicates=args.num_replicates,
	groups=groups,
	savefile='results/gnk_{}_L{}_q{}_V{}_K{}_r{}_n{}s{}'.format(args.model_name, args.L, args.q, args.Vstr, args.K, args.num_replicates, args.max_num_samples, args.num_samples_step))

print('Time elapsed: {}'.format(datetime.now() - start_time))