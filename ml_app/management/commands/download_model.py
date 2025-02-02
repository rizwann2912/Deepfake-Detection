import os
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Download the deepfake detection model"

    def handle(self, *args, **kwargs):
        models_folder = os.path.join(settings.BASE_DIR, 'models')
        model_file_path = os.path.join(models_folder, 'model_87_acc_20_frames_final_data.pt')

        os.makedirs(models_folder, exist_ok=True)

        if not os.path.exists(model_file_path) or os.path.getsize(model_file_path) == 0:
            print("Downloading deepfake model...")

            file_id = "13WKWR3r8cM9DeguLoKXOumsi1gSQgKnm"
            file_url = f"https://drive.google.com/uc?export=download&id={file_id}"

            try:
                # Use wget instead of gdown
                subprocess.run(["wget", file_url, "-O", model_file_path], check=True)
                
                if os.path.exists(model_file_path) and os.path.getsize(model_file_path) > 0:
                    print("✅ Model downloaded successfully!")
                else:
                    print("❌ Model download failed! File might be empty.")
            except Exception as e:
                print(f"❌ Error downloading model: {e}")
        else:
            print("✅ Model already exists.")

