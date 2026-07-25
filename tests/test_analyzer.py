import unittest
import requests
from unittest.mock import patch
from analyzer import analyze_website


class TestAnalyzer(unittest.TestCase):

    def test_valid_url(self):
        """Happy Path"""

        result = analyze_website("https://example.com")

        self.assertEqual(result["status"], 200)
        self.assertIn("title", result)
        self.assertIn("response_time", result)

    def test_url_without_https(self):
        """URL without https://"""

        result = analyze_website("example.com")

        self.assertEqual(result["status"], 200)

    def test_invalid_url(self):
        """Invalid URL"""

        result = analyze_website("invalid-url-xyz")

        self.assertIn("status", result)

    @patch("requests.get")
    def test_timeout(self, mock_get):
        """Simulate timeout"""

        mock_get.side_effect = requests.exceptions.Timeout()

        result = analyze_website("https://example.com")

        self.assertEqual(result["status"], "Timeout")


if __name__ == "__main__":
    unittest.main()