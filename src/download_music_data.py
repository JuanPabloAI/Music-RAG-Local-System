import os
from datasets import load_dataset
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def download_and_save():
    print("Download dataset from Hugging Face...")

    dataset = load_dataset("seungheondoh/LP-MusicCaps-MSD", split='train')

    # Convert to DataFrame
    df = pd.DataFrame(dataset)

    # Save in data/raw folder
    raw_path = "data/raw/music_data_raw.csv"
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(raw_path, index=False)

    print(f"Dataset downloaded and saved to {raw_path}")

if __name__ == "__main__":
    download_and_save()