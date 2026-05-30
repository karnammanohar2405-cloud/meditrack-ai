def detect_wastage(reports):
    total = len(reports)

    unused_stock = 0
    overstock = 0

    for r in reports:
        stock = r[2]

        if stock > 150:
            overstock += 1
        if stock == 0:
            unused_stock += 1

    return {
        "overstock_hospitals": overstock,
        "critical_empty": unused_stock,
        "wastage_risk_score": round((overstock / total) * 100, 2) if total else 0
    }