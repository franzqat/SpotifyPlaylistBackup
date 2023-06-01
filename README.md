# SpotifyPlaylistBackup
This project allows you to copy the contents of a Spotify playlist to another existing playlist (could be useful for the Discover Weekly playlist). It utilizes the Spotipy library for interacting with the Spotify API and the Telegram bot for sending notifications. The project can be run as a Docker container.

## Prerequisites

Before running the project, make sure you have the following prerequisites:

- Spotify Developer Account:
  - Create a Spotify Developer account at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
  - Create a new application to obtain the client ID and client secret.
  - Set the Redirect URI in the Spotify application settings to `http://localhost:8888/callback/`.

- Telegram Bot:
  - Create a Telegram bot using the BotFather.
  - Obtain the bot token for accessing the Telegram Bot API.

- Docker:
  - Install Docker on your machine. Refer to the [Docker documentation](https://docs.docker.com/get-docker/) for instructions specific to your operating system.

## Configuration

Configure the project by setting the required environment variables. Create a `.env` file in the project directory with the following content:

```plaintext
SPOTIFY_CLIENT_ID=<Your Spotify Client ID>
SPOTIFY_CLIENT_SECRET=<Your Spotify Client Secret>
TELEGRAM_BOT_TOKEN=<Your Telegram Bot Token>
TELEGRAM_CHAT_ID=<Get it from https://api.telegram.org/bot<Your Telegram Bot Token>/getUpdates> after creating the bot and using the /start command.
SPOTIFY_SOURCE_PLAYLIST=<Your Source Spotify playlist UID>
SPOTIFY_DEST_PLAYLIST=<Your Destination Spotify playlist UID>
```

Note: To acquire the Spotify playlist ID you can browse <https://open.spotify.com/>, open a playlist then copy the id after `playlist/`:
Something like `https://open.spotify.com/playlist/1234567abcdefg`. In this case: `1234567abcdefg`

## Usage

1. Clone the project repository:

   ```shell
   git clone https://github.com/your-username/playlist-backup.git
   ```

2. Navigate to the project directory:

   ```shell
   cd playlist-backup
   ```

3. Build the Docker image:

   ```shell
   docker build -t playlist-backup .
   ```

4. Run the Docker container:

   ```shell
   docker run --env-file .env playlist-backup
   ```

   The container will start and perform the playlist backup process. Once completed, a Telegram message will be sent with the list of copied songs.

5. Check the destination playlist in your Spotify account to verify the copied songs.

## Notes 

🔒 Security Notice: Project Scanned with Trivy

This project has undergone a security scan using Trivy, a vulnerability scanner for container images and systems. Trivy helps identify potential security issues and vulnerabilities within the project dependencies.

The scan was performed to ensure that known vulnerabilities are addressed and to promote the usage of secure and up-to-date packages. However, please note that the scan does not guarantee the absence of all security risks.

## Contributing

Contributions to this project are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).