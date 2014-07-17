# for model building:
def get_model():
    # Read in and build the model automatically from the histograms in the root file. 
    # This model will contain all shape uncertainties given according to the templates
    # which also includes rate changes according to the alternate shapes.
    # For more info about this model and naming conventuion, see documentation
    # of build_model_from_rootfile.
    model = build_model_from_rootfile('dilep_GKK.root',include_mc_uncertainties=True)

    # If the prediction histogram is zero, but data is non-zero, teh negative log-likelihood
    # is infinity which causes problems for some methods. Therefore, we set all histogram
    # bin entries to a small, but positive value:
    model.fill_histogram_zerobins()

    # define what the signal processes are. All other processes are assumed to make up the 
    # 'background-only' model.
    # model.set_signal_processes('Zprime*')
    model.set_signal_processes('RSgluon*')

    # Add some lognormal rate uncertainties. The first parameter is the name of the
    # uncertainty (which will also be the name of the nuisance parameter), the second
    # is the 'effect' as a fraction, the third one is the process name. The fourth parameter
    # is optional and denotes the channl. The default '*' means that the uncertainty applies
    # to all channels in the same way.
    # Note that you can use the same name for a systematic here as for a shape
    # systematic. In this case, the same parameter will be used; shape and rate changes 
    # will be 100% correlated.

    model.add_lognormal_uncertainty('ttbar_xsec',     0.15, 'ttbar'    )
    model.add_lognormal_uncertainty('DY_norm',        1.00, 'DY'       )
    model.add_lognormal_uncertainty('singletop_xsec', 0.50, 'singletop')
    model.add_lognormal_uncertainty('VV_xsec',        0.30, 'VV'       )

    for p2 in model.processes:
        model.add_lognormal_uncertainty('lumi', 0.026, p2)

    # Specifying all uncertainties manually can be error-prone. You can also execute
    # a automatically generated file using python's execfile here
    # which contains these statements, or read in a text file, etc. Remember: this is a
    # python script, so use this power!
    return model

model = get_model()

# first, it is a good idea to generate a summary report to make sure everything has worked
# as expected. The summary will generate quite some information which should it make easy to spot
# errors like typos in the name of uncertainties, missing shape uncertaintie, etc.
model_summary(model)

# 2. apply the methods

# 2.a. Bayesian limits
# Calculate expected and observed Bayesian limits. For faster run time of this example,
# only make a few mass points. (Omitting the 'signal_procsses' parameter completely would
# process all signals defined as signal processes before; see Section "Common Parameters"
# on the theta auto intro doxygen page for details)

# plot_exp, plot_obs = bayesian_limits(model, signal_process_groups = {'zp2000':['zp2000']})
plot_exp, plot_obs = bayesian_limits(model)

# parVals = mle(model, 'data', n=1)
# print parVals

# plot_exp and plot_obs are instances of plotutil.plotdata. they contain x/y values and
# bands. You can do many things with these objects such as inspect the x/y/ban
# data, pass then to plotutil.plot routine to make pdf plots, ...
# Here, we will just create text files of the plot data. This is useful if you want
# to apply your own plotting routines or present the result in a text Table.
plot_exp.write_txt('bayesian_limits_expected.txt')
plot_obs.write_txt('bayesian_limits_observed.txt')

# 2.b. CLs limits
# calculate cls limit plots. The interface is very similar to bayesian_limits. However, there are a few
# more options such as the definition of the test statistic which is usually a likelihood ratio but can differ in
# which parameters are minimized and which constraints / ranges are applied during minimization.
# Here, we stay with the default which fixes beta_signal=0
# for the background only hypothesis and lets it float freely for the signal+background hypothesis.
# See cls_limits documentation for more options.

#plot_exp, plot_obs = cls_limits(model, ts='lhclike', signal_processes = [['zp750'], ['zp1000'], ['zp1250'], ['zp1500'], ['zp2000'], ['zp3000']])
#plot_exp, plot_obs = cls_limits(model, ts='lhclike', signal_processes = [['zp500'], ['zp750'], ['zp1000'], ['zp1250'], ['zp1500'], ['zp2000'], ['zp3000'], ['zp4000']])

# as for the bayesian limits: write the result to a text file
#plot_exp.write_txt('cls_limits_expected.txt')
#plot_obs.write_txt('cls_limits_observed.txt')

# model_summary, bayesian_limits, and cls_limits also write their results to the 'report' object
# which we can ask to write its results as html page to a certain directory. Use an existing, empty
# directory and point your web browser to it.
report.write_html('htmlout')

# After running theta-auto, you probably want to delete the 'analysis' directory which
# contains intermediate results. Keeping it avoids re-running theta unnecessarily for unchanged configurations
# (e.g., because you just want to change the plot). However, this directory can grow very large over time.


