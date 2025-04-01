from flask import Flask, jsonify, request
from scrapper.scraper import FlexibleScraper

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_page():
    url = request.args.get('url')  # Reçoit l'URL en tant que paramètre de chaîne de requête
    if not url:
        return jsonify({"error": "L'URL est obligatoire."}), 400

    scraper = FlexibleScraper(url)
    raw_text = scraper.scrape()

    if raw_text:
        return jsonify({"content": raw_text}), 200
    else:
        return jsonify({"error": "Impossible d'obtenir le contenu"}), 400

# Fonction principale qui sera appelée par la commande en ligne de commande
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
