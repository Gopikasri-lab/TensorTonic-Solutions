def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    ref_count = sum(reference_counts)
    prod_count = sum(production_counts)
    reference_counts = [i/ref_count for i in reference_counts]
    production_counts = [i/prod_count for i in production_counts]     
    tvd = 0.5*sum(abs(p-r) for p,r in zip(production_counts,reference_counts))
    f = tvd>threshold
    drift = {"score":tvd,"drift_detected":f}
    return drift
    