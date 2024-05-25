# Bot Discord - Bonjour Madame
Ce bot Discord récupère automatiquement l'image et le titre du dernier post sur le site [BonjourMadame](https://bonjourmadame.fr/) et les publie dans un channel Discord.

## Installation
### Prérequis
- Docker
- Docker Compose
- Token discord [Discord developers portal](https://discord.com/developers/applications)

### Instructions
```bash
# Clonez ce dépôt
git clone https://github.com/votre_utilisateur/bonjourmadame-discord-bot.git

# Accédez au répertoire du projet
cd bonjourmadame-discord-bot

# Créez un fichier .env à la racine du projet et ajoutez-y les variables d'environnement suivantes :
# Remplacez votre_token_discord par votre token Discord et votre_channel_id par l'ID du channel Discord où vous souhaitez que le bot publie les messages
echo "DISCORD_TOKEN=votre_token_discord" > .env
echo "DISCORD_CHANNEL_ID=votre_channel_id" >> .env

# Build le conteneur
docker-compose build

# Executer le conteneur
docker-compose run --rm bonjour-madame
```
<br>

## Automatisation
Il est recommandé d'utiliser un cronjob ou un autre type de schedule pour automatiser l'usage de ce bot
