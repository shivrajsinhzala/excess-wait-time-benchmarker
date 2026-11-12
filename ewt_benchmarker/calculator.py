"""
Excess Wait Time (EWT) Calculator
Implements standard FTA & Transport for London (TfL) service regularity benchmark methodology:
    SWT = sum(H_sched^2) / (2 * sum(H_sched))
    AWT = sum(H_actual^2) / (2 * sum(H_actual))
    EWT = AWT - SWT
"""

import math
from typing import List, Dict, Any


def compute_average_waiting_time(headways: List[float]) -> float:
    """Calculates passenger-weighted expected wait time for a list of headways."""
    if not headways:
        return 0.0
    sum_h = sum(headways)
    sum_h_sq = sum(h * h for h in headways)
    if sum_h == 0:
        return 0.0
    return sum_h_sq / (2.0 * sum_h)


def run_ewt_benchmark(scheduled_headways: List[float], actual_headways: List[float]) -> Dict[str, Any]:
    """
    Compares scheduled vs actual headways to compute standard transit regularity KPIs.
    """
    if not scheduled_headways or not actual_headways:
        raise ValueError("Both scheduled and actual headway sequences are required.")

    swt = compute_average_waiting_time(scheduled_headways)
    awt = compute_average_waiting_time(actual_headways)
    ewt = max(0.0, awt - swt)

    mean_sched = sum(scheduled_headways) / len(scheduled_headways)
    mean_actual = sum(actual_headways) / len(actual_headways)

    # Bunching threshold: actual < 50% of scheduled mean
    bunching_threshold = 0.5 * mean_sched
    bunching_count = sum(1 for h in actual_headways if h < bunching_threshold)

    # Gap threshold: actual > 150% of scheduled mean
    gap_threshold = 1.5 * mean_sched
    gap_count = sum(1 for h in actual_headways if h > gap_threshold)

    # Punctuality / Regularity ratio
    regularity_ratio = swt / awt if awt > 0 else 1.0

    return {
        "scheduled_trips": len(scheduled_headways),
        "actual_trips": len(actual_headways),
        "mean_scheduled_headway_min": round(mean_sched, 2),
        "mean_actual_headway_min": round(mean_actual, 2),
        "scheduled_wait_time_swt_min": round(swt, 3),
        "actual_wait_time_awt_min": round(awt, 3),
        "excess_wait_time_ewt_min": round(ewt, 3),
        "regularity_ratio": round(regularity_ratio, 4),
        "bunching_events": bunching_count,
        "bunching_rate_pct": round((bunching_count / len(actual_headways)) * 100, 2),
        "gap_events": gap_count,
        "gap_rate_pct": round((gap_count / len(actual_headways)) * 100, 2)
    }
