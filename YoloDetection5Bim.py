import cv2
from ultralytics import YOLO


class DetectionObjets:
    def __init__(self, chemin_modele='yolov8s.pt', seuil_confiance=0.5):
        """
        Initialise le modèle YOLOv8 et définit le seuil de confiance.

        :param chemin_modele: Chemin vers le fichier du modèle YOLOv8
        :param seuil_confiance: Seuil de confiance pour les détections
        """
        self.modele = YOLO(chemin_modele)
        self.seuil_confiance = seuil_confiance

    def detecter_objets_dans_image(self, image):
        """
        Détecte les objets dans une image et retourne l'image avec les détections.

        :param image: Image à traiter
        :return: Image avec les détections
        """
        resultats = self.modele(image)

        for resultat in resultats:
            for det in resultat.boxes:
                x1, y1, x2, y2 = map(int, det.xyxy[0])
                confiance = det.conf[0]
                classe = int(det.cls[0])
                etiquette = self.modele.names[classe]

                # Définir la couleur de la boîte en fonction de l'objet détecté
                if etiquette == 'laptop':
                    couleur = (0, 0, 255)  # Rouge pour laptop
                elif etiquette == 'mouse':
                    couleur = (255, 0, 0)  # Bleu pour souris
                else:
                    couleur = (200, 66, 116)  # Violet pour les autres objets

                # Dessiner la boîte de détection et le label sur l'image
                cv2.rectangle(image, (x1, y1), (x2, y2), couleur, 2)
                cv2.putText(image, f'{etiquette} {confiance:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, couleur, 2)

        return image

    def detecter_objets_dans_video(self, source_video=0):
        """
        Détecte les objets dans un flux vidéo et affiche les résultats en temps réel.

        :param source_video: Chemin du fichier vidéo ou index de la caméra
        """
        cap = cv2.VideoCapture(source_video)
        if not cap.isOpened():
            print(f"Erreur : Impossible d'ouvrir la vidéo {source_video}")
            return

        while cap.isOpened():
            ret, image = cap.read()
            if not ret:
                break

            # Détecter les objets dans l'image actuelle
            image = self.detecter_objets_dans_image(image)
            # Afficher l'image avec les détections
            cv2.imshow('Détections - Projet5BIM', image)

            # Quitter la boucle si 'q' est pressé
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Chemin vers le flux vidéo ou index de la caméra (0 pour la caméra par défaut donc la Webcam)
    source_video = 0  # ou 'path_to_video.mp4' pour un fichier vidéo

    # Crée l'objet de détection et démarre la détection des objets dans le flux vidéo de la Webcam
    detecteur = DetectionObjets()
    detecteur.detecter_objets_dans_video(source_video)
