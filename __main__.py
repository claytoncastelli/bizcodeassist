from module2.module2 import function_from_module2
from scrapper.scraper import FlexibleScraper


def main():
    print("Iniciando o projeto...")

    result2 = function_from_module2()
    print(result2)


    # Instanciation du scraper pour les pages statiques
    # url = "https://www.lapresse.ca/"
    # url = "https://www.odq.qc.ca/trouver-un-dentiste/"
    url = "https://forums.docker.com/t/docker-private-registry-how-to-list-all-images/21136"
    scraper = FlexibleScraper(url=url, scroll_infinite=True)
    # Effectuer un scraping de page
    content = scraper.scrape()
    # Afficher le contenu extrait
    print("************************************************************")
    print(content)


if __name__ == "__main__":
    main()
