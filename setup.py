# from distutils.core import setup
# from setuptools import setup, find_packages
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="bizcodeassist",  # Le nom du package
    version="0.1.0",  # Version du package
    description="Outil d’aide à l’identification des codes d’activités pour les souscripteurs",
    author="Clayton Casteli, Renato Suga, Fakhri Dridi, Francis Duval",
    author_email="2191680@csfoy.ca, 1894556@csfoy.ca, 2196840@csfoy.ca, francis_duval@cooperators.ca",
    url="https://github.com/claytoncastelli/bizcodeassist",  # URL du référentiel.
    packages=find_packages(),  # Il trouvera automatiquement tous les packages et sous-packages
    install_requires=[  # Dépendances de votre projet
        "pytest>=6.2.5", # Tests
        'flask==2.2.2',  # Flask
        'beautifulsoup4==4.11.1',  # BeautifulSoup
        "requests==2.32.0",  # Requests
        'selenium==4.7.0',  # Selenium
        'webdriver-manager==3.8.3',  # WebDriver Manager
        'googletrans==4.0.0-rc1',  #Googletrans
        'mtranslate',   #MTranslate
        'transformers', #MarianMT
        'sentencepiece',
        'torch',
        'hf_xet'
        'setuptools >= 38.6.0',
        'wheel >= 0.31.0',
        'twine >= 1.11.0',
        'build',
    ],
    # tests_require=[  # Dépendances spécifiques aux tests
    #     "pytest>=6.2.5",
    # ],
    extras_require={  # Dépendances supplémentaires (facultatif)
        "dev": [
            "flake8>=3.8.4",  # Outil d'analyse de code
            "black>=21.9b0",  # Outil de formatage de code
            "tox>=3.24.5",  # Outil d'automatisation des tests
        ],
    },
    entry_points={
        'console_scripts': [
            'bizcodeassist = bizcodeassist.app:main',  # Commande pour exécuter l'API
        ],
    },
    classifiers=[  # Classifications des projets (facultatif)
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Spécifie la version minimale de Python
    include_package_data=True,  # Inclut des fichiers supplémentaires (par exemple, des fichiers statiques)
    long_description= long_description,  # Lire la documentation README
    long_description_content_type="text/markdown",  # Format du README
)
