import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
# sns.scatterplot(x='total_bill', y='tip', hue='sex', data=df, color='blue', marker='o', s=100)
# plt.show()

# sns.lineplot(x='size', y='tip', hue='sex', data=df, color='red', marker='o', linestyle='--', linewidth=2, markersize=8)
# plt.show()


# sns.countplot(x='day', data=df, palette='Set2')
# plt.show()

# sns.countplot(x='day', data=df, hue='sex')
# plt.show()

# sns.barplot(x='day', y='total_bill', data=df, palette='Set1')
# plt.show()

# sns.boxenplot(x='day', y='total_bill', data=df, palette='Set3')
# plt.show()

corr=df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.show()