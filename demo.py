import mcmc_tc
import mcmc_plot
import numpy as np
import matplotlib.pyplot as plt
import csv

#data prep
with open('example_data.csv', 'rb') as csvfile:
    csvobj = csv.reader(csvfile)
    header = csvobj.next()
    data = []
    for row in csvobj:
        data.append(row)
        
#convert data to np arrays
data = np.array(data)
data = data.astype(np.float)

#select a voxel and the stimulus conditions
voxel_num = 497
y = data[:,voxel_num+3]
x = 2*(np.pi/180)*((data[:,3]-1)*20)#multiply condition number by 20 degrees (and scale to 360 for the vm)

#run mcmc
sampler_vm = mcmc_tc.mcmc_est(y,x,mcmc_tc.vm_func,mcmc_tc.log_like_addgauss, ndim=5)
sampler_flat = mcmc_tc.mcmc_est(y,x,mcmc_tc.flat_func,mcmc_tc.log_like_addgauss, ndim=2)

#model comparison (calc evidence for tuned model, bf > 10 is good evidence)
bf = mcmc_tc.bayes_factor(sampler_vm, sampler_flat)
print(bf)

#calc fwhm of vm model
vmf = 0.5*mcmc_tc.vm_fwhm(sampler_vm.flatchain[:,3])#0.5 bevause vm is across 2pi
vm_max, vm_min = mcmc_tc.vm_maxmin(sampler_vm.flatchain)
vmb = vm_min#baseline BOLD
vma = vm_max-vm_min#amplitude

##plot results
burnin = 1000#first 1000 samples 'burning in'
f, ax = plt.subplots(1, 2, figsize=(15,6))
mcmc_plot.mcmc_plot_model(ax[0], y, x, sampler_vm.flatchain[burnin:,:], mcmc_tc.vm_func)
mcmc_plot.mcmc_plot_scatter(ax[1], vma[burnin:], vmf[burnin:])
plt.show()

