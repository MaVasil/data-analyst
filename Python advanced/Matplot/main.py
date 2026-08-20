import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Chart: Line chart
# What it does: Connects data points to show a trend or change over an ordered axis.
# When to use it: Use it for values that change over time or another continuous sequence.
# plt.plot(x, y,color='red', marker='o', linestyle='--', linewidth=2, markersize=8)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple Plot")
# plt.show()

# Chart: Scatter plot
# What it does: Displays individual points to show the relationship between two variables.
# When to use it: Use it to find correlations, clusters, gaps, or unusual values.
# plt.scatter(x, y, color='blue', marker='o', s=100)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot")
# plt.show()

# Chart: Bar chart
# What it does: Compares the size of values across separate categories.
# When to use it: Use it when the categories are distinct, such as products, regions, or subjects.
# plt.bar(x, y, color='green', width=0.5)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Bar Chart")
# plt.show()

# Chart: Histogram
# What it does: Groups numeric values into intervals and counts how many values fall in each interval.
# When to use it: Use it to understand the distribution, spread, and shape of numerical data.
# marks = [32, 45, 48, 51, 55, 56, 62, 65, 67, 70, 72, 75, 80, 85, 90]
# plt.hist(marks, bins=3)

# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.title("Distribution of Marks")

# plt.show()

# Chart: Pie chart
# What it does: Shows how categories contribute to a complete total using slices.
# When to use it: Use it for a small number of categories when their percentages add up to 100%.
# sizes=[15, 30, 45, 10]
# labels=['xxl', 'xl', 'l', 'm']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Pie Chart")
# plt.show()

# Chart: Multiple-line chart
# What it does: Draws several lines so related trends can be compared on the same axes.
# When to use it: Use it to compare changes between products, groups, or measurements.
y2=[12,18,22,28]

# plt.plot(x,y,label='Product 1',color='red',marker='o',linestyle='--',linewidth=2,markersize=8)
# plt.plot(x,y2,label='Product 2',color='blue',marker='s',linestyle='-',linewidth=2,markersize=8)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line Plot")
# plt.legend()
# plt.show()


# fig,axes=plt.subplots(2,1,figsize=(5,4))
# axes[0].plot(x,y,label='Product 1',color='red',marker='o',linestyle='--',linewidth=2,markersize=8)
# axes[0].set_title("Product 1")

# axes[1].plot(x,y2,label='Product 2',color='blue',marker='s',linestyle='-',linewidth=2,markersize=8)
# axes[1].set_title("Product 2")
# plt.show()


plt.figure(figsize=(8, 4), dpi=100)
# plt.style.use('dark_background')
plt.plot(x, y)
plt.grid(True)
# plt.xlim(0, 5)
# plt.ylim(0, 35)
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 5, 10, 15, 20, 25, 30, 35])
# plt.savefig('line_chart.png', dpi=300, bbox_inches='tight')

plt.savefig('line_chart2.png', dpi=300)
plt.show()
print("Line chart saved as 'line_chart2.png' with 300 dpi and tight bounding box.")