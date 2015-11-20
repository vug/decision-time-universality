# decision-time-universality
A small study to observe the universality in Google search query durations.

This script makes Google search queries of randomly chosen words and records their durations into a file. 

## Usage
- Edit `googledecisionduration.py` to set the number of words. 
- Run it via `python googledecisionduration.py`. 
- After it finishes you can plot the graph via `python googledecisionduration_plot.py`.

# Example
Here is the distribution for 1874 words.

![alt distribution of normalized durations](https://raw.github.com/vug/decision-time-universality/master/distribution.png)

# References
The definition of universality can be seen in this paper: [Universality in Numerical Computations with Random Data. Case Studies](http://arxiv.org/abs/1407.3829)
