# barplots, pointplots and countplots

# The final group of categorical plots are barplots, pointplots and countplot which create statistical summaries of the data. The plots follow a similar API as the other plots and allow further customization for the specific problem at hand.

# •	Create a countplot with the df dataframe and Model Selectedon the y axis and the color varying by Region.

# Show a countplot with the number of models used with each region a different color
sns.countplot(data=df,
         y="Model Selected",
         hue="Region")

plt.show()
plt.clf()

# •	Create a pointplot with the df dataframe and Model Selectedon the x-axis and Award_Amount on the y-axis.
# •	Use a capsize in the pointplot in order to show the confidence interval.
sns.pointplot(data=df,
         x='Model Selected',
         y='Award_Amount',
         capsize=.1)

plt.show()
plt.clf()

# •	Create a barplot with the same data on the x and y axis and change the color of each bar based on the Region column.

# Create a barplot with each Region shown as a different color
sns.barplot(data=df,
         y='Award_Amount',
         x='Model Selected',
         hue='Region')

plt.show()
plt.clf()