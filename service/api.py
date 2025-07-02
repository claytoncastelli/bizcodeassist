from flask import Flask, jsonify, request
from scrapper.scraper import FlexibleScraper
from text_processing.translator.translator_factory import TranslatorFactory
from text_processing.translator.translator_type import TranslatorType
from text_processing.summarizer.summarizer_factory import SumarizerFactory
from text_processing.summarizer.summarizer_type import SummarizerType

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

@app.route('/summarise', methods=['GET'])
def summarize_page():
    url = request.args.get('url')  # Reçoit l'URL en tant que paramètre de chaîne de requête
    if not url:
        return jsonify({"error": "L'URL est obligatoire."}), 400

    scraper = FlexibleScraper(url)
    raw_text = scraper.scrape()

    baseTranslator = TranslatorFactory().create_translator(TranslatorType.MARIANMT)
    translate_text = baseTranslator.translate(raw_text)
    print("Translator:\n", translate_text)

    sumarizer = SumarizerFactory.create_sumarizer(SummarizerType.BART_CNN)
    summary = sumarizer.summarize(translate_text)
    print("Summary:\n", summary)

    # sumarizer = SumarizerFactory.create_sumarizer(SummarizerType.MT5_BASE)
    # summary = sumarizer.summarize(translate_text)
    # print("Summary:\n", summary)

    if raw_text:
        return jsonify({"content": summary}), 200
    else:
        return jsonify({"error": "Impossible d'obtenir le contenu"}), 400

# Fonction principale qui sera appelée par la commande en ligne de commande
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
