import numpy as np
import matplotlib.pyplot as plt

def mcmc_plot_scatter(ax, vma, vmf):
    """Plot the MCMC samples of Amplitude and FWHM parameters"""
    
    #scatter plot
    ax.plot(vma, vmf, ',r', alpha=0.1)
    
    #show the median
    ax.plot(np.median(vma), np.median(vmf), 'ko', markersize=5)
    
    #formatting
    ax.set_xlabel(r'Amplitude ($\beta$)')
    ax.set_ylabel('FWHM (Degrees)')
    yticklocs = [0, np.pi/4, np.pi/2]
    yticklabs = [0, 45, 90]
    ax.set_yticks(yticklocs)
    ax.set_yticklabels(yticklabs)
    ax.set_xlim([0, 2])
   
    
def mcmc_plot_model(ax, y, x, samples, tuning_foo, num_sample_plots=300):
    """Plot the VM model samples and median as 'best fit'"""

    #define the linspace for plotting
    xplot = np.linspace(0, 2*np.pi, 100)

    #plot the sampled models
    for row in samples[np.random.randint(len(samples), size=num_sample_plots)]:
       ax.plot(xplot, tuning_foo(xplot,row[:-1]), color="r", alpha=0.1)


    #plot the median model from the samples
    med_theta = np.median(samples, axis=0)
    ax.plot(xplot, tuning_foo(xplot, med_theta[:-1]), color='k', linewidth =3, \
         label = (r'Median p($\Theta$|y)'))

    #plot the data
    ax.plot(x, y, 'b+', label = 'Data')

    #format
    ax.set_xlim([0,2*np.pi])
    ax.set_xlabel('Stimulus Orientation (Degrees)')
    ax.set_ylabel(r'$\beta$')
    xticklocs = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xticklabs = [0, 45, 90, 135, 180]
    ax.set_xticks(xticklocs)
    ax.set_xticklabels(xticklabs)
