#!/usr/bin/env python3
import argparse
import json
import sys
from ewt_benchmarker.calculator import run_ewt_benchmark


def main():
    parser = argparse.ArgumentParser(description="Benchmark transit Excess Wait Time (EWT) and headway regularity.")
    parser.add_argument("--scheduled", "-s", nargs="+", type=float, required=True, help="List of scheduled headways (min)")
    parser.add_argument("--actual", "-a", nargs="+", type=float, required=True, help="List of observed actual headways (min)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    try:
        report = run_ewt_benchmark(args.scheduled, args.actual)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

    if args.json:
        print(json.dumps(report, indent=2))
        return

    print("==================================================")
    print(" 📊 Transit Excess Wait Time (EWT) Benchmark")
    print("==================================================")
    print(f" Scheduled Wait Time (SWT):  {report['scheduled_wait_time_swt_min']} min")
    print(f" Actual Wait Time (AWT):     {report['actual_wait_time_awt_min']} min")
    print(f" Excess Wait Time (EWT):     {report['excess_wait_time_ewt_min']} min")
    print(f" Regularity Ratio:           {report['regularity_ratio']}")
    print(f" Bunching Events:            {report['bunching_events']} ({report['bunching_rate_pct']}%)")
    print(f" Gap Events:                 {report['gap_events']} ({report['gap_rate_pct']}%)")
    print("==================================================")
    print(" ⏱️  Ecosystem Analytics: https://headway.shivrajsinh.in")
    print(" 🚆 Transit Platform:    https://transit.shivrajsinh.in")
    print("==================================================")


if __name__ == "__main__":
    main()
