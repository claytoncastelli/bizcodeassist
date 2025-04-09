from module2.module2 import function_from_module2
from scrapper.scraper import FlexibleScraper
import scrapper.company_scraper 

def main():
    print("Iniciando o projeto...")

    result2 = function_from_module2()
    print(result2)


    # # Example of calling company_scraper
    url = "https://www.cooperators.ca"  # Replace with the URL you want to scrape
    description_entreprise = scrapper.company_scraper.creer_description_entreprise(url)
    print("Description générée :\n", description_entreprise)
    

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
