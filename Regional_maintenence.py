# N Roberts
# DAD 220

import matplotlib.pyplot as plt
import numpy as np

# Data from your analysis
regions = ["Midwest", "Southeast", "Northeast", "West", "Southwest"]
replacement_counts = [260, 208, 208, 66, 63]

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(replacement_counts, labels=regions, autopct="%1.1f%%", colors=["blue", "red", "green", "orange", "purple"], startangle=140)

# Add title
plt.title("Regional Distribution of Part Replacements")

# Show the pie chart
plt.show()