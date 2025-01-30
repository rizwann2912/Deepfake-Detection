from django.conf import settings
import os
import gdown

class MlAppConfig(AppConfig):
    name = 'ml_app'

    def ready(self):
        # Get the models folder dynamically inside the Django project directory
        models_folder = os.path.join(settings.BASE_DIR, 'models')
        model_file_path = os.path.join(models_folder, 'model_87_acc_20_frames_final_data.pt')

        # Ensure the models folder exists
        os.makedirs(models_folder, exist_ok=True)

        # Check if the model file exists; if not, download it
        if not os.path.exists(model_file_path):
            print("Deepfake model not found. Downloading...")
            try:
                file_url = 'https://drive.google.com/uc?id=16rayULoKYjRx8Ww3B2uE3eiFnKWxodN4'
                gdown.download(file_url, model_file_path, quiet=False)
                print(f"Model downloaded successfully to {model_file_path}.")
            except Exception as e:
                print(f"Error downloading model: {e}")
        else:
            print("Deepfake model already exists.")
