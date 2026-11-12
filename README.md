# Excess Wait Time (EWT) Benchmarker

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://github.com/shivrajsinhzala/excess-wait-time-benchmarker/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Transit Engine](https://img.shields.io/badge/Ecosystem-Headway_&_Stopwatch-orange.svg)](https://headway.shivrajsinh.in)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/shivrajsinhzala/excess-wait-time-benchmarker/pulls)

> Industry-standard public benchmark suite measuring transit Scheduled Wait Time (SWT), Actual Wait Time (AWT), and Excess Wait Time (EWT) across high-frequency bus and metro corridors.

---

## ⏱️ What is Excess Wait Time (EWT)?

On high-frequency transit lines (where vehicles arrive every 12 minutes or less), commuters generally do not consult a fixed timetable; they arrive at stops randomly. Standard on-time punctuality (within 5 minutes of schedule) fails to reflect passenger delay when vehicles bunch together.

Transport authorities (including Transport for London and US Federal Transit Administration) measure high-frequency service quality using **Excess Wait Time (EWT)**:

$$\text{SWT} = \frac{\sum H_{\text{sched}}^2}{2 \sum H_{\text{sched}}}$$
$$\text{AWT} = \frac{\sum H_{\text{actual}}^2}{2 \sum H_{\text{actual}}}$$
$$\text{EWT} = \text{AWT} - \text{SWT}$$

Where $H$ is the interval between consecutive departures. When buses bunch, $\sum H_{\text{actual}}^2$ inflates, directly capturing the extra minutes passengers waste on the platform.

This benchmark suite powers:
- ⏱️ **[Headway Engine](https://headway.shivrajsinh.in)**: Real-time headway regularity analytics, EWT calculation, and bunching prediction.
- 🚆 **[Stopwatch Transit](https://transit.shivrajsinh.in)**: Commuter live arrival tracking and schedule reliability indexer.

---

## 📦 Installation

```bash
pip install excess-wait-time-benchmarker
```

---

## 🚀 Python Usage

```python
from ewt_benchmarker import run_ewt_benchmark

# Compare scheduled 10-minute headway against observed real-time arrivals
report = run_ewt_benchmark(
    scheduled_headways=[10.0, 10.0, 10.0, 10.0, 10.0],
    actual_headways=[3.0, 17.0, 4.0, 16.0, 10.0]
)

print(f"Scheduled Wait Time (SWT): {report['scheduled_wait_time_swt_min']} min")
print(f"Actual Wait Time (AWT):    {report['actual_wait_time_awt_min']} min")
print(f"Excess Wait Time (EWT):    {report['excess_wait_time_ewt_min']} min")
print(f"Regularity Ratio:          {report['regularity_ratio']}")
print(f"Bunching Rate:             {report['bunching_rate_pct']}%")
```

---

## 💻 CLI Usage

```bash
ewt-benchmark --scheduled 10 10 10 10 --actual 4 16 5 15
```

---

## 🔗 Related Transit Projects

- **[Headway](https://headway.shivrajsinh.in)**: Commuter wait-time optimization, Welch-Paull headway calculation, and regularity benchmarking.
- **[Stopwatch Transit](https://transit.shivrajsinh.in)**: Real-time public transit tracking, live bus telemetry, and zero-latency timetable PWA.
- **[Welch-Paull Headway Calculator](https://github.com/shivrajsinhzala/welch-paull-headway-calculator)**: Queueing theory waiting time equations.

---

## 📄 License

MIT © [Shivrajsinh Zala](https://github.com/shivrajsinhzala)
