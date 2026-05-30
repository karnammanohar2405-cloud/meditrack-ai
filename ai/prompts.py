SHORTAGE_ANALYSIS_PROMPT = """
You are a healthcare analytics assistant.

Analyze the government hospital medicine reports.

Provide:

1. Most unavailable medicines
2. High-risk hospitals
3. Repeated shortage patterns
4. Availability trends
5. Recommendations

Data:

{data}
"""