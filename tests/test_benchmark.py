import unittest
from ewt_benchmarker.calculator import run_ewt_benchmark, compute_average_waiting_time

class TestEwtBenchmarker(unittest.TestCase):
    def test_zero_excess_wait(self):
        # Perfect clockface compliance: scheduled == actual
        sched = [10.0, 10.0, 10.0, 10.0]
        actual = [10.0, 10.0, 10.0, 10.0]
        res = run_ewt_benchmark(sched, actual)
        self.assertEqual(res["excess_wait_time_ewt_min"], 0.0)
        self.assertEqual(res["regularity_ratio"], 1.0)
        self.assertEqual(res["bunching_events"], 0)

    def test_bunching_degradation(self):
        # Actual experiences bunching: 2 min and 18 min
        sched = [10.0, 10.0, 10.0, 10.0]
        actual = [2.0, 18.0, 2.0, 18.0]
        res = run_ewt_benchmark(sched, actual)
        self.assertGreater(res["excess_wait_time_ewt_min"], 1.0)
        self.assertLess(res["regularity_ratio"], 1.0)
        self.assertEqual(res["bunching_events"], 2)

if __name__ == "__main__":
    unittest.main()
