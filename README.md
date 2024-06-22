
# Système de Détection d'Ordinateurs et de Souris

Ce projet s'inscrit dans le cadre de l'Unité d'enseignement 5BIM et utilise OpenCV et YOLOv8 pour détecter des ordinateurs et des souris dans le flux vidéo de la webcam du PC. Il est supervisé par Monsieur Allan BUSI.


## Prérequis

Assurez-vous d'avoir les versions de Python et des bibliothèques suivantes installées:

- Python 3.7+
- OpenCV 4.5 ou supérieur : Pour la capture vidéo et le traitement d'images avec OpenCV.
- Torch : Pour le support PyTorch, nécessaire pour le modèle YOLOv8.
- Torchvision : Pour les utilitaires PyTorch liés à la vision par ordinateur.
- YOLOv8 (via ultralytics) : Pour utiliser le modèle YOLOv8.

Dans le cas contraire, vous pouvez installer les dépendances nécessaires avec:

pip install -r requirements.txt


Ensuite pour éxecuter le code python, utilisez le commande :

python .\YoloDetection5Bim.py 


### Structure du Code

Le code est divisé en plusieurs parties :

- DetectionObjets: Classe principale pour gérer la détection d'objets.
- __init__: Initialise le modèle YOLOv8 et définit le seuil de confiance.
- detecter_objets_dans_image: Méthode pour détecter des objets dans une image.
- detecter_objets_dans_video: Méthode pour traiter le flux vidéo de la webcam ou d'un fichier vidéo et appliquer la détection d'objets en temps réel.
- main: Fonction principale pour lancer la détection d'objets dans le flux vidéo de la webcam.


#### Remarques

Les étiquettes des classes pour les ordinateurs et les souris sont "laptop" et "mouse" dans le modèle YOLOv8. Je les ai identifié respectivement par les couleurs "Rouge" et "Bleu" pendant la détection.