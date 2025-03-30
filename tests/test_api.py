
### 5. **Testes**
#```python
import unittest
from module3.api import app

class TestScrapingAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_scrape_success(self):
        # url = "https://www.lapresse.ca/"
        url = "https://centredentairestefoy.com/traitement-de-canal-au-centre-dentaire-Sainte-Foy/?gad_source=1&gclid=CjwKCAjwnPS-BhBxEiwAZjMF0kgrmvWbvU4de4ni3inMBZ48leNxEL3rmuOdz-QaJhegBNbZVBTgSRoCoF8QAvD_BwE#Accueil"
        response = self.app.get(f"/scrape?url={url}")
        # response = self.app.get(f"/scrape?url=https://www.lapresse.ca/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.json)

    def test_scrape_failure(self):
        response = self.app.get('/scrape')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
