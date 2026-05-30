def calculate_reach_score(reports):
    total = len(reports)

    available = len([r for r in reports if r[3] == "Available"])
    low = len([r for r in reports if r[3] == "Low Stock"])
    out = len([r for r in reports if r[3] == "Out of Stock"])

    if total == 0:
        return {
            "reach_score": 0,
            "shortage_rate": 0
        }

    reach_score = (available / total) * 100
    shortage_rate = ((low + out) / total) * 100

    return {
        "reach_score": round(reach_score, 2),
        "shortage_rate": round(shortage_rate, 2)
    }