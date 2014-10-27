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
Includes:<br>
mcmc_tc.py - routines for estimating Von Mises model parameters.<br>
mcmc_plot.py - plotting the results of previous analysis<br>
demo.py - demonstration of fitting a Von Mises function to a single voxel using real fMRI data. Also computes the Bayes factor of the Von Mises model over an untuned model<br>
example_data.csv - data from an orientation tuning experiment. Columns 3 to end are detrended and z-normalised BOLD timeseries for each voxel in V1 of this subject (V1 voxels were isolated using retinotopic mapping in a separate analysis)


