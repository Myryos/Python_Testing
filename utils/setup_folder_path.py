import os


def setup_reports_folders():
    root_dir = "reports"

    subfolders = ["coverage", "locust", "media", "media/coverage", "media/locust"]

    for folder in subfolders:
        folder_path = os.path.join(root_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")
