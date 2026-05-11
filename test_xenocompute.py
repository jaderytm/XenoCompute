# test_xenocompute.py
"""
Tests for XenoCompute module.
"""

import unittest
from xenocompute import XenoCompute

class TestXenoCompute(unittest.TestCase):
    """Test cases for XenoCompute class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XenoCompute()
        self.assertIsInstance(instance, XenoCompute)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XenoCompute()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
