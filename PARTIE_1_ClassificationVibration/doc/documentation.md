# Documentation du Projet de Classification des Vibrations (Horizontal et Vertical)

Ce projet a pour objectif de classifier les vibrations horizontales et verticales détectées par un accéléromètre. Les données sont collectées à l'aide d'une carte Arduino, traitées et utilisées pour entraîner un modèle de classification. Ce modèle est ensuite exporté pour être intégré sur la même carte Arduino afin de réaliser des inférences en temps réel. 

La structure du projet est divisée en plusieurs parties, chacune responsable d'une étape clé du processus. Voici un aperçu détaillé de cette structure.


### Détails des Composants

#### 1. `PARTIE_1_ClassificationVibrations/`

Ce répertoire principal contient tous les fichiers liés à la partie du projet où les vibrations sont collectées, analysées et utilisées pour entraîner un modèle de classification, puis pour réaliser des inférences en temps réel sur une carte Arduino.

#### 2. `README.md`

Le fichier `README.md` situé dans la racine de `PARTIE_1_ClassificationVibrations/` fournit des explications générales sur le projet, sa structure, son objectif, et comment utiliser les différents fichiers. Ce fichier sert d'introduction pour l'ensemble du projet.

#### 3. `1-DataGeneration_Arduino/`

Ce répertoire contient tout le code nécessaire pour la génération et la collecte des données de vibration à partir d'un accéléromètre connecté à la carte Arduino. Les données collectées comprennent les valeurs d'accélération dans les trois axes (X, Y, Z), qui seront utilisées pour l'entraînement du modèle.

- **Fichier principal** : `data_generation.ino` : Ce code Arduino est chargé de lire les données depuis l'accéléromètre, de les formater et de les enregistrer dans un fichier de sortie (typiquement sous forme de fichier CSV) pour une analyse ultérieure.

#### 4. `2-Training/`

Ce répertoire est responsable de la préparation et de l'entraînement du modèle de classification des vibrations. Il comprend plusieurs sous-dossiers essentiels pour ce processus :

- **`dataset/`** : Ce dossier contient les données d'entraînement collectées via Arduino. Une fois que les vibrations ont été générées et collectées, elles sont stockées ici pour être utilisées dans l'entraînement du modèle.
  
- **`notebooks/`** : Ce dossier contient des fichiers Jupyter Notebook pour faciliter l'analyse des données et l'entraînement du modèle. Le fichier principal `training_vibrations.ipynb` est utilisé pour effectuer l'analyse exploratoire des données, nettoyer les données brutes et entraîner un modèle de réseau de neurones pour classifier les vibrations horizontales et verticales.

- **`models/`** : Ce dossier contient les modèles entraînés sous différents formats (par exemple, `.h5` pour un modèle complet ou `.tflite` pour la version TensorFlow Lite destinée à être utilisée sur Arduino). Une fois l'entraînement terminé, le modèle est sauvegardé dans ce répertoire.

#### 5. `3-Inference_Arduino/`

Ce répertoire contient le code nécessaire pour utiliser le modèle entraîné sur la carte Arduino afin de faire des inférences en temps réel. Une fois que le modèle est exporté sous un format compatible avec Arduino (comme un fichier `.h` ou `.tflite`), ce répertoire contient le code Arduino nécessaire pour charger et utiliser ce modèle sur la carte afin de classer les vibrations pendant l'exécution.

- **Fichier principal** : `inference_vibrations.ino` : Ce code charge le modèle exporté et effectue des prédictions sur les données en temps réel générées par l'accéléromètre.

#### 6. `doc/`

Le dossier `doc/` contient la documentation détaillée du projet. Cela inclut des explications sur les différentes étapes du projet, des schémas, des illustrations et des détails supplémentaires qui peuvent être utiles pour comprendre le fonctionnement du projet. Le fichier principal `documentation.md` fournit une explication complète du projet, de sa structure, et des étapes nécessaires pour utiliser le projet de manière optimale.

## Explication du Processus

### 1. Collecte des Données (Arduino)

Dans la première partie du projet, l'Arduino collecte les données d'accélération de l'accéléromètre et un code python écoute le port série connécté avec la carte arduino pour l'enregistrement des données dans un fichier CSV. Cela permet de créer un ensemble de données qui peut ensuite être utilisé pour l'entraînement du modèle. 
J'ai collécté des donnée pour les vibration verticale et horizontale.

### 2. Entraînement du Modèle

Une fois que les données ont été collectées, Elles sont traité et préparé pour l'entrainement. Une partie des données sera pour l'apprentissage et l'autre pour le teste.
Un modèle de réseau de neurones est défini et entraîné sur les données d'entrainement pour classer les vibrations en catégories horizontales ou verticales. 
![Capture d’écran (1111)](https://github.com/user-attachments/assets/f1c6ae40-55f9-4d79-a338-3761140f92c2)

Ce modèle a une petite taille et simple, mais suffisamment performant pour effectuer des prédictions en temps réel sur Arduino.
![Capture d’écran (1112)](https://github.com/user-attachments/assets/8abb1937-3c49-46e2-b779-cb457e2419a9)


### 3. Inférence en Temps Réel (Arduino)

Le modèle entraîné est exporté au format `.h`, puis importé avec un code Arduino pour effectuer des inférences en temps réel. L'Arduino prends les valeurs de l'accéléromètre, applique le modèle et classe les vibrations.

## Conclusion

Ce projet montre comment collecter des données de vibration, les utiliser pour entraîner un modèle de classification, puis déployer ce modèle sur une carte Arduino pour réaliser des inférences en temps réel. 


