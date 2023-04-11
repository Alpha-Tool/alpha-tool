from pyupdater.hooks import base_hook

# Configurez PyUpdater pour utiliser GitHub comme source de mise à jour
UPLOADER_CONFIG = {
    "uploader": "github",
    "repo_name": "https://github.com/Alpha-Tool/alpha-tool.git",
    "username": "meupiyouronald@gmail.com",
    "password": "2Ron@ld6",
}

# Créez un hook pour inclure les fichiers nécessaires à la mise à jour
@base_hook
def include_files():
    # Ajoutez les fichiers nécessaires à la mise à jour
    return ["new.py"]
