#Nilaris Roberts
#DAD 220

#Stakeholders for Fleet Maintenance Visualization
import matplotlib.pyplot as plt

# Data
parts = ["Tires", "Windshield", "Wheel Arch", "Fender", "Rocker Panel"]
replacements = [66, 63, 55, 54, 53]

# bar chart
plt.figure(figsize=(6, 3), dpi=150)  # Higher DPI (150)
plt.bar(parts, replacements, color=['blue', 'red', 'orange', 'green', 'purple'])

# Labels and formatting
plt.xlabel("Parts", fontsize=9)
plt.ylabel("Replacements", fontsize=9)
plt.title("Most Replaced Parts", fontsize=10)

# Adjust y labels for readability
plt.xticks(rotation=0, fontsize=8)
plt.yticks(fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()