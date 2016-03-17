import numpy as np
from scipy.interpolate import interp1d
import pdb

###
### lambda interpolation
###
def lambda_interpol(lambda_input,lambda_set,throughput_set,min_lambda,max_lambda):
	sub_select = (lambda_input > min_lambda) & \
					(lambda_input < max_lambda)
	lambda_select = lambda_input[sub_select]
	f = interp1d(lambda_set,throughput_set,kind='linear')
	throughput_filter_new = f(lambda_select)
	return throughput_filter_new,sub_select

###
### convolve filter throughput, see Yi et al. 1995 PASP
###

def convolve_filter(lambda_filter,throughput_filter,lambda_input,flux_input,fluxErr_input):

	min_lambda_filter,max_lambda_filter = min(lambda_filter),max(lambda_filter)
	throughput_filter_new,sub_select = lambda_interpol(lambda_input,lambda_filter,throughput_filter,min_lambda_filter,max_lambda_filter)

	lambda_select = lambda_input[sub_select]
	flux_select = flux_input[sub_select]
	fluxErr_select = fluxErr_input[sub_select]
	subsub = np.isfinite(flux_select)

	dlambda_input = lambda_select[1:]-lambda_select[:-1]
	tmp = dlambda_input.tolist()
	tmp.extend([tmp[0]])
	dlambda_input = np.array(tmp)
	numer = np.sum(flux_select[subsub]*throughput_filter_new[subsub]* \
						lambda_select[subsub]*dlambda_input[subsub])
	numer_err = np.sqrt(np.sum((fluxErr_select[subsub]* \
					throughput_filter_new[subsub]* \
					lambda_select[subsub]*dlambda_input[subsub])**2.))
	denom = np.sum(throughput_filter_new[subsub]*lambda_select[subsub]*dlambda_input[subsub])
	f_filter = numer/denom
	fErr_filter = numer_err/denom
	return f_filter,fErr_filter

