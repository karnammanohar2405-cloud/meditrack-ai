def calculate_efficiency(reports):
    total = len(reports)

    if total == 0:
        return 0

    available = len([r for r in reports if r[3] == "Available"])
    low = len([r for r in reports if r[3] == "Low Stock"])
    out = len([r for r in reports if r[3] == "Out of Stock"])

    # Weighted scoring system
    score = (
        (available * 1.0) +
        (low * 0.5) +
        (out * 0.0)
    ) / total * 100

    return round(score, 2)
