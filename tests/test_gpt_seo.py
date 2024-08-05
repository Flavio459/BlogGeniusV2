import unittest
from unittest.mock import patch, Mock
from scripts.agents.gpt_seo import load_keywords_from_csv, identify_keywords

class TestGPTSEO(unittest.TestCase):

    def test_load_keywords_from_csv(self):
        file_path = 'path_to_your_file.csv'  # Atualize com o caminho correto do arquivo CSV
        keywords = load_keywords_from_csv(file_path)
        self.assertGreater(len(keywords), 0)
        self.assertIn('keyword', keywords[0])

    @patch('time.sleep', return_value=None)
    @patch('pytrends.request.TrendReq')
    def test_identify_keywords(self, MockTrendReq, mock_sleep):
        mock_trendreq_instance = MockTrendReq.return_value
        mock_trendreq_instance.interest_over_time.return_value = pd.DataFrame({
            'date': ['2022-01-01', '2022-02-01'],
            'python automation': [50, 70]
        })

        identify_keywords()
        mock_trendreq_instance.build_payload.assert_called()

if __name__ == '__main__':
    unittest.main()
