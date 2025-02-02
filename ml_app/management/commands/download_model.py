from django.core.management.base import BaseCommand
import os
import gdown
from django.conf import settings

class Command(BaseCommand):
    help = "Download the deepfake detection model"

    def handle(self, *args, **kwargs):
        # Define the model's directory and file path
        models_folder = os.path.join(settings.BASE_DIR, 'models')
        model_file_path = os.path.join(models_folder, 'model_87_acc_20_frames_final_data.pt')

        # Create the models folder if it doesn't exist
        os.makedirs(models_folder, exist_ok=True)

        # Check if the model file already exists
        if not os.path.exists(model_file_path):
            print("Downloading deepfake model...")
            try:
                file_url = "https://drive.google.com/uc?id=16rayULoKYjRx8Ww3B2uE3eiFnKWxodN4"
                gdown.download(file_url, model_file_path, quiet=False)
                print("Model downloaded successfully!")
            except Exception as e:
                print(f"Error downloading model: {e}")
        else:
            print("Model already exists.")
