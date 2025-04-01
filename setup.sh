#!/bin/bash

# Sortie d'erreur si quelque chose échoue
set -e

# Mettre à jour pip, setuptools et wheel (s'ils ne sont pas mis à jour)
echo "Updating pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

# Installer les dépendances du projet
echo "Installing project dependencies..."
pip install -r requirements.txt

# Générer le fichier .whl (Wheel) du projet
echo "Building the .whl file..."
python setup.py bdist_wheel

# Afficher où le fichier .whl a été généré
echo "Wheel file generated in the 'dist' directory:"
ls dist/

# (Facultatif) Exécutez le projet dans Docker
# echo "Running the project in Docker..."
# docker-compose up --build