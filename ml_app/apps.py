from django.apps import AppConfig
import os
import gdown


class MlAppConfig(AppConfig):
    name = 'ml_app'

    def ready(self):
        # Path to the models folder
        models_folder = r'C:\Users\mdriz\deepfake\deepfake_detection\Django Application\models'
        model_file_path = os.path.join(models_folder, 'model_87_acc_20_frames_final_data.pt')

        # Ensure the models folder exists
        if not os.path.exists(models_folder):
            os.makedirs(models_folder)

        # Check if the model file exists, if not, download it
        if not os.path.exists(model_file_path):
            print("Deepfake model not found. Downloading...")
            try:
                # Google Drive file URL (with your file ID)
                file_url = 'https://drive.google.com/uc?id=16rayULoKYjRx8Ww3B2uE3eiFnKWxodN4'
                
                gdown.download(file_url, model_file_path, quiet=False)
                print(f"Deepfake model downloaded successfully to {model_file_path}.")
            except Exception as e:
                print(f"Error downloading deepfake model: {e}")
        else:
            print("Deepfake model already exists.")
