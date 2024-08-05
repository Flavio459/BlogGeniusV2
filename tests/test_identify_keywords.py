import unittest
from unittest.mock import patch, Mock
import json
import pandas as pd
from scripts.agents.gpt_seo import identify_keywords

class TestIdentifyKeywords(unittest.TestCase):

    @patch('pytrends.request.TrendReq')
    @patch('requests.Session.post')
    @patch('requests.Session.get')
    def test_identify_keywords(self, mock_get, mock_post, mock_TrendReq):
        # Mock para a requisição de cookies do Google Trends
        mock_cookie_response = Mock()
        mock_cookie_response.cookies.items.return_value = [('NID', 'test-cookie')]
        mock_get.return_value = mock_cookie_response

        # Mock para Google Trends
        mock_trend_req = mock_TrendReq.return_value
        mock_trend_req.interest_over_time.return_value = pd.DataFrame({
            'date': ['2022-01-01', '2022-01-02'],
            'python automation': [100, 75]
        }).set_index('date')
        mock_trend_req.GENERAL_URL = 'https://trends.google.com/trends/api/explore'
        mock_trend_req.build_payload.return_value = None

        # Mock para o método post
        mock_post_response = Mock()
        mock_post_response.status_code = 200
        mock_post_response.headers = {'Content-Type': 'application/json'}
        mock_post_response.json.return_value = {"widgets": [{"request": {}}]}
        mock_post.return_value = mock_post_response

        # Chamar a função que estamos testando
        identify_keywords()

        # Verificar se o arquivo 'keywords.json' foi criado corretamente
        with open('keywords.json', 'r') as f:
            keywords = json.load(f)

        # Verificar se os dados do Google Trends estão corretos
        self.assertEqual(keywords[0]['python automation'], 100)

if __name__ == '__main__':
    unittest.main()
