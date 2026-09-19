import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import unittest

from analysis.analyze_expert_ratings import exact_agreement, fleiss_kappa, weighted_kappa


class AgreementAnalysisTests(unittest.TestCase):
    def test_perfect_agreement(self) -> None:
        ratings = {"A": "Mandatory", "B": "Recommended", "C": "Optional"}
        raters = [ratings, dict(ratings), dict(ratings)]
        item_ids = sorted(ratings)

        self.assertAlmostEqual(fleiss_kappa(raters, item_ids), 1.0)
        self.assertAlmostEqual(exact_agreement(ratings, ratings, item_ids), 1.0)
        self.assertAlmostEqual(weighted_kappa(ratings, ratings, item_ids), 1.0)

    def test_opposite_ordinal_ratings_have_no_exact_agreement(self) -> None:
        left = {"A": "Mandatory", "B": "Mandatory"}
        right = {"A": "Optional", "B": "Optional"}

        self.assertEqual(exact_agreement(left, right, ["A", "B"]), 0.0)


if __name__ == "__main__":
    unittest.main()
