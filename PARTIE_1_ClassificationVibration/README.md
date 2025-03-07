Détection et Classification des Vibrations avec Arduino Nano 33 BLE et TensorFlow Lite

## **Description du projet**

Ce projet a pour objectif de concevoir un système de détection et de classification des vibrations, en utilisant la carte **Arduino Nano 33 BLE** et son **IMU intégré** . Le projet comporte plusieurs parties, allant de la génération des données, à l'entraînement d'un modèle de machine learning, jusqu'à l'inférence en temps réel sur la carte Arduino. Le modèle de classification, basé sur TensorFlow Lite, permettra de classer des vibrations en deux catégories : **vibrations verticales** et **vibrations horizontales**.

## **Structure du projet**

Le projet est structuré comme suit :

├── PARTIE_1_ClassificationVibrations/  
│   ├── README.md                     # Explications spécifiques à la partie 1
│   ├── 1-DataGeneration_Arduino/     
│   │   ├── data_generation.ino       # Code Arduino pour la génération/collecte de données
│   ├── 2-Training/                  
│   │   ├── dataset/                  # Contient les données d'entraînement (collectées via Arduino)
│   │   ├── notebooks/                
│   │   │   └── training_vibrations.ipynb  # Jupyter Notebook pour l'entraînement du modèle
│   │   ├── models/                   # Modèle(s) issu(s) de l'entraînement (format .tflite, etc.)
│   ├── 3-Inference_Arduino/         
│   │   ├── inference_vibrations.ino  # Code Arduino pour faire l’inférence en temps réel
│   └── doc/                          
│       └── documentation.md          # Documentation détaillée, explications, schémas, etc.

