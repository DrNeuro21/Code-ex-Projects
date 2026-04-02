import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age_Range": ["11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "46-50",
                  "51-55", "56-60", "61-65", "66-70", "71-75", "76-80", "81-85", "86-90",
                  "91-95", "96-100"],
    "Impact_Men": [12, 10, 10, 12, 14, 16, 18, 20, 22, 25, 28, 31, 35, 40, 45, 50, 55, 60],
    "Impact_Women": [14, 12, 13, 15, 17, 19, 22, 25, 28, 30, 33, 36, 40, 45, 50, 55, 60, 65]
})

plt.figure(figsize=(12, 6))
plt.plot(df["Age_Range"], df["Impact_Men"], marker='o', label="Men")
plt.plot(df["Age_Range"], df["Impact_Women"], marker='x', color='red', label="Women")
plt.xlabel("Age Range")
plt.ylabel("Time to Impact (Minutes)")
plt.title("Caffeine Impact Time Trend by Age and Sex")
plt.legend()
plt.xticks(rotation=45)

p = base_path + "caffeine_line_plot.png"
print(p)

plt.savefig(p)
plt.show()
plt.close()


plt.figure(figsize=(8,5))

plt.hist([df["Impact_Men"], df["Impact_Women"]], bins=10, label=['Men', 'Women'], color=['blue', 'red'], alpha=0.7)
plt.xlabel("Impact Time (Minutes)")
plt.ylabel("Frequency")
plt.title("Histogram of Caffeine Impact Times")
plt.grid(axis='y', alpha=0.75)
plt.legend()

hist_path = base_path + "caffeine_histogram.png"
plt.savefig(hist_path)
plt.show()
plt.close()
