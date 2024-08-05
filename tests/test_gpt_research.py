import unittest
from unittest.mock import patch
import json  # Certifique-se de que o módulo json está importado
from scripts.agents.gpt_research import research_blogs

class TestGPTResearch(unittest.TestCase):

    @patch('scripts.agents.gpt_research.requests.get')
    def test_research_blogs(self, mock_get):
        # Mock a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'results': ['Blog 1', 'Blog 2']}

        research_blogs()

        with open('blogs.json', 'r') as f:
            blogs = json.load(f)

        self.assertEqual(blogs, ['Blog 1', 'Blog 2'])

    @patch('scripts.agents.gpt_research.requests.get')
    def test_research_blogs_failure(self, mock_get):
        # Mock a failed API response
        mock_get.return_value.status_code = 404

        with self.assertRaises(SystemExit) as cm:
            research_blogs()

        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
