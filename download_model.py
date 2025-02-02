from django.core.management.base import BaseCommand
import os
import gdown
from django.conf import settings

class Command(BaseCommand):
    help = "Download model file"

    def handle(self, *args, **kwargs):
        models_folder = os.path.join(settings.BASE_DIR, 'models')
        model_file_path = os.path.join(models_folder, 'model_87_acc_20_frames_final_data.pt')

        os.makedirs(models_folder, exist_ok=True)

        if not os.path.exists(model_file_path):
            print("Downloading deepfake model...")
            gdown.download("https://drive.google.com/uc?id=16rayULoKYjRx8Ww3B2uE3eiFnKWxodN4", model_file_path, quiet=False, fuzzy=True)
            print("Download complete!")
        else:
            print("Model already exists.")
