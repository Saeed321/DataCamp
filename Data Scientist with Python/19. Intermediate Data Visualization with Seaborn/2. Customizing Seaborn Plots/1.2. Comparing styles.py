# Comparing styles

# Seaborn supports setting different styles that can control the aesthetics of the final plot. In this exercise, you will plot the same data in two different styles in order to see how the styles change the output.

# Create a distplot() of the fmr_2 column using a dark style. After showing the plot, use plt.clf() to clear the figure.
sns.distplot(df['fmr_2'])
sns.set_style('dark')
plt.clf()
plt.show()

# Create the same distplot() of fmr_2 using a whitegrid style. Clear the plot after showing it.
sns.distplot(df['fmr_2'])
sns.set_style('whitegrid')
plt.show()
plt.clf()