tuning_curve_analysis
=====================

Set of functions for fitting a Von Mises function to characterise orientation tuning in visual cortex. 
Example fMRI data is given which includes the currently viewed orientation and associated BOLD response of voxels in V1. 
demo.py uses Bayesian MCMC estimation to find parameters of a Von Mises function that best account for the tuning 
properties of a single voxel.<br>
<br>
Dependencies:<br>
numpy<br>
matplotlib.pyplot<br>
emcee<br>
csv<br>
<br>
Includes:
mcmc_tc.py - routines for estimating Von Mises model parameters.<br>
mcmc_plot.py - plotting the results of previous analysis<br>
demo.py - demonstration of the functionality - fitting a Von Mises function to a single voxel using real fMRI data
                                                also computes the Bayes factor of the Von Mises model over untuned<br>
example_data.csv - data from an orientation tuning experiment. Columns 3 to end are Beta parameters of a GLM fit to that
                    presentation of the grating stimulus. The data used in practice could be raw BOLD time series or 
                    firing rates


