import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, urljoin
import time
import re


class FlexibleScraper:
    def __init__(self, url, scroll_infinite=False, min_content_size=500, max_depth=2):
        """
        Initialisez le scraper avec une URL du site, une option de défilement infini, ou le minimum de contenu,
        et une profondeur maximale pour rechercher d'autres pages sur mon site.
        """
        self.url = url
        self.scroll_infinite = scroll_infinite
        self.min_content_size = min_content_size
        self.max_depth = max_depth  # Define a profundidade máxima de páginas a serem visitadas

        # Armazena os links já visitados para evitar scraping repetido
        self.visited_links = set()

    def _get_html(self):
        """
        Fonction pour obtenir le HTML de la page. Utilisez les requêtes pour les pages statiques et Selenium pour les pages dynamiques.
        """
        html = self._get_html_with_requests()

        if html and len(html) < self.min_content_size:
            print(f"Le contenu détecté est inférieur {self.min_content_size}, tentative d'utilisation de Selenium...")
            return self._get_html_with_selenium()

        return html

    def _get_html_with_requests(self):
        """
        Obtient le code HTML à l'aide des requêtes pour les pages statiques.
        """
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'accès à la page avec les requêtes: {e}")
        return None

    def _get_html_with_selenium(self):
        """
        Obtient le HTML en utilisant Selenium (sans ouvrir la fenêtre du navigateur).
        Peut inclure un défilement/scroll infini si nécessaire.
        """
        options = Options()
        options.add_argument('--headless')  # Rodar sem abrir a janela do navegador
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(self.url)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except TimeoutException:
            print("Le temps d'attente dépassé. La page ne s'est pas chargée comme prévu.")
            driver.quit()
            return None

        time.sleep(2)  # Delai d'attente de 2 seconds pour assurer que la page se charge.

        if self.scroll_infinite:
            self._scroll_infinite(driver)

        html = driver.page_source
        driver.quit()
        return html

    def _scroll_infinite(self, driver):
        """
        Effectue un défilement infini sur la page.
        """
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script("return document.body.scrollHeight") > last_height)
            time.sleep(2)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def _extract_text(self, soup):
        """
        Função para extrair o texto da página.
        """
        return soup.get_text().strip()

    def _extract_internal_links(self, soup):
        """
        Fonction pour extraire le text de la page.
        """
        internal_links = set()
        base_url = urlparse(self.url).netloc
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(self.url, href)
            # Vérifie si le lien est interne au domaine
            if urlparse(full_url).netloc == base_url:
                internal_links.add(full_url)
        return internal_links

    def scrape_page(self, url, current_depth=0):
        """
        Fonction principale pour gratter une page, et également rechercher des pages internes.
        """
        if current_depth > self.max_depth:
            return ""

        # Evita visitar a mesma página mais de uma vez
        if url in self.visited_links:
            return ""
        self.visited_links.add(url)

        print(f"Scraping/Grattage de pages: {url}")
        self.url = url  # Mettre à jour l'URL de la nouvelle page
        html = self._get_html()

        if html:
            soup = BeautifulSoup(html, 'html.parser')
            content = self._extract_text(soup)

            # Extrait les liens internes et effectue un scraping récursif
            internal_links = self._extract_internal_links(soup)
            for link in internal_links:
                if link not in self.visited_links:
                    content += "\n\n" + self.scrape_page(link, current_depth + 1)

            return content
        else:
            return "Impossible d'accéder à la page."

    def remove_white_spaces(self, content):
        """
        Supprimer les espaces multiples entre les mots.
        """
        if content:
            content = re.sub(r"\n+", "\n", content)
            content = "\n".join(" ".join(line.split()) for line in content.splitlines())
        return content


    def scrape(self):
        """
        Démarrez le processus de scraping à l’URL initiale et recherchez les pages internes.
        """
        return self.remove_white_spaces(self.scrape_page(self.url))
