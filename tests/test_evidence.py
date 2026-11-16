import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reproducibility'))
from verify import verify

class EvidenceTests(unittest.TestCase):
    def test_curated_evidence_is_internally_consistent(self):
        self.assertTrue(verify())

if __name__=='__main__':
    unittest.main()
