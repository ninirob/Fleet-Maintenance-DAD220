

import numpy as np
import matplotlib.pyplot as plt

# Data from your analysis
part_names = ["Wheel Arch", "Fender", "Rocker Panel", "Windshield", "Dent Repairs"]
corrosion_counts = [55, 54, 53, 0, 0]  # Corrosion-related replacements
accident_counts = [0, 0, 0, 63, 62]  # Accident-related replacements

# Set up bar positions
x = np.arange(len(part_names))  # Creates numerical positions for each part
width = 0.4  # Width of each bar

plt.figure(figsize=(8, 5))

# Plot bars
plt.bar(x - width/2, corrosion_counts, width, label="Corrosion", color="blue")
plt.bar(x + width/2, accident_counts, width, label="Accident", color="red")

# Add labels and title
plt.xlabel("Parts")
plt.ylabel("Number of Replacements")
plt.title("Corrosion vs. Accident-Related Replacements")
plt.xticks(x, part_names)  # Set part names as x-axis labels
plt.legend()

# Show the chart
plt.show()