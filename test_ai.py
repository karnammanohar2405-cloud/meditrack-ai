from ai.groq_analysis import analyze_shortages

sample_data = """
District Hospital, Paracetamol, Out of Stock
District Hospital, Paracetamol, Out of Stock
Area Hospital, Insulin, Low Stock
Community Health Centre, Paracetamol, Out of Stock
"""

result = analyze_shortages(sample_data)

print("\nAI ANALYSIS:\n")
print(result)