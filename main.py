from scrape_module.module1 import function_from_module1
from module2.module2 import function_from_module2
from module3.module3 import function_from_module3
from scrape_module.scraper import FlexibleScraper


def main():
    print("Iniciando o projeto...")

    result1 = function_from_module1()
    result2 = function_from_module2()
    result3 = function_from_module3()

    print(result1)
    print(result2)
    print(result3)

    # Instanciation du scraper pour les pages statiques
    # url = "https://www.lapresse.ca/"
    url = "https://www.odq.qc.ca/trouver-un-dentiste/"

    scraper = FlexibleScraper(url=url, scroll_infinite=True)

    # Effectuer un scraping de page
    content = scraper.scrape()

    # Afficher le contenu extrait
    print("************************************************************")
    print(content)


if __name__ == "__main__":
    main()
