import matplotlib.pyplot as plt

# Quarterly data
quarters = ["Q1", "Q2", "Q3", "Q4"]
turnover = [3.72, 3.90, 2.81, 7.19]
industry_target = 8

# Calculate average
avg_turnover = sum(turnover) / len(turnover)
print(f"Average Turnover: {avg_turnover:.2f}")

# Plot
plt.figure(figsize=(8,6))
plt.plot(quarters, turnover, marker="o", label="Company Turnover", linewidth=2)
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (8)")

plt.title("Quarterly Inventory Turnover Ratio - 2024")
plt.xlabel("Quarter")
plt.ylabel("Turnover Ratio")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save chart
plt.savefig("turnover_chart.png", dpi=300, bbox_inches="tight")
plt.show()
