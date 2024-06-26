import os
import shutil

def delete_files_and_folders(directory):
    """
    Delete all files and folders within a specified directory except for a file named 'best_model.zip'.

    Parameters
    ----------
    directory : str
        The path to the directory from which files and folders are to be deleted.

    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file != "best_model.zip":
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if not any("best_model.zip" in f for f in os.listdir(os.path.join(root, dir))):
                shutil.rmtree(os.path.join(root, dir))

delete_files_and_folders("/scratch/abhijeet/bunkermanagement/PPO_CL/ppo_paper_draft/models/ppo")
delete_files_and_folders("/scratch/abhijeet/bunkermanagement/PPO_CL/ppo_paper_draft/models/ppo_volume_criteria")
