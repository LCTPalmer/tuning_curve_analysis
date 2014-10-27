#MCMC estimation of tuning curves

import numpy as np
import emcee
#from scipy.special import jn

###---Tuning Models---###
def vm_func(x,theta_tc):
    """
    Von Mises distribution----------
    x = sample point
    theta_tc = parameter vector of the function, in the following order:
    base = baseline
    amp = amplitude multiplier
    loc = location
    kappa = spread
    """
    base, amp, loc, kappa = theta_tc
    return base + amp * np.exp(kappa * np.cos(x-loc))
    #/ 2*np.pi*jn(0, kappa))
     
def flat_func(x, theta_tc):
    """
    Untuned distribution--------
    theta_tc = 1 parameter: baseline
    """
    base = theta_tc
    return base*np.ones(len(x))

###---Von Mises analysis---###
def vm_fwhm(kappa):
    """
    Full-width at half maximum for the Von Mises function
    """
    t1 = 0.5*np.exp(kappa)
    t2 = 0.5*np.exp(-1*kappa)
    return 2*np.arccos(np.log(t1+t2)/kappa)

def vm_maxmin(theta):
    """
    Find the maximum and minimum of the Von Mises function with the given
    parameters.
    theta = [baseline amplitude location kappa] 
    """
    vm_max = []
    vm_min = []
    for base, amp, loc, kappa, junk in theta:
        vm_max.append(base+amp*np.exp(kappa))
        vm_min.append(base+amp*np.exp(-kappa))
    return np.array(vm_max), np.array(vm_min)

###---Probability Distributions---###
def log_like_addgauss(theta, y, x, tuning_foo):
    """
    Likelihood with additive Gaussian noise model----------
    theta = parameter vector for tuning function with noise model variance appended
    y = true data points
    x = sample points
    tuning_foo = name of tuning function
    """
    #split the theta into tuning and noise parameters
    theta_tc = theta[:-1]
    sigma = theta[-1]
    #calc the model output
    y_model = tuning_foo(x, theta_tc)
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) \
                         + (y - y_model) ** 2 / sigma ** 2)

def log_prior(theta):
    """
    Prior on parameters---------
    in our case just return -inf if certain params are negative
    """
    for param in theta[1:]: #starting from 1, as baseline is first
        if param < 0:
            return -np.inf
        
    if len(theta) > 2:#if we are looking at the VM func
        if theta[2] > 2*np.pi:#if the location is greater than 2pi
            return -np.inf
        
    return 0

def log_posterior(theta, y, x, tuning_foo, like_foo):
    """
    Log-posterior distribution
    """
    return log_prior(theta) + like_foo(theta, y, x, tuning_foo)

###--MCMC Estimation and Selection---###
def mcmc_est(y, x, tuning_foo, like_foo, ndim=5, nwalkers=100, nsteps=2000):
    """
    Runs MCMC estimation of posterior over model parameters
    Takes in the true data, y, at sampling points, x, along with
    handle of the candidate tuning model and handle of the likelihood ]
    function
    """
    np.random.seed(0)
    starting_guesses = np.random.random((nwalkers, ndim))
    sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, \
                                args=[y, x, tuning_foo, like_foo])
    sampler.run_mcmc(starting_guesses, nsteps)
    return sampler

def bayes_factor(sampler_model1, sampler_model2):
    """
    Calculates the bayes factor between two models
    Candidate model emcee objects are inputs
    Output is p(d|M1)/p(d|M2), approximated as the ratio
    of harmonic means in the MCMC sampling chains
    """
    support_model1 = np.mean(np.exp(sampler_model1.flatlnprobability))
    support_model2 = np.mean(np.exp(sampler_model2.flatlnprobability))
    return support_model1/support_model2




