# Weaviate Devcontainer Template

This is a template for creating a Weaviate devcontainer / Codespace, with Docker containers.

## How to run

Option 1: Devcontainer
Option 2: Github Codespaces

### Option 1: Devcontainer

1. Install Docker
2. Install VSCode
3. Install Devcontainer extension
4. Open this repository in VSCode
5. Open the command palette (Ctrl/Cmd+Shift+P), and select "Dev Containers: Rebuild and Reopen in Container"
6. Wait for the container to build and start

### Option 2: Github Codespaces

1. Click on the green "Code" button in the top right corner of the repository
2. Select "Open with Codespaces"
3. Click on "New codespace"
4. Wait for the codespace to build and start

## How to run Weaviate

### Option 1: Docker (in devcontainer)

1. Open a terminal (in the devcontainer or codespace)
2. Run the following command to start Weaviate:
   ```bash
   ./run-weaviate.sh start
   ```
3. Wait for Weaviate to start (it will show a message on the terminal when finished)

### Option 2: Weaviate Cloud

1. Go to the [Weaviate Cloud Console](https://console.weaviate.cloud/) and create a new Weaviate instance (e.g. the Sandbox is free)
2. Once the instance is created, click on it to open the instance details
3. Connect to it using the Weaviate client using those details.

## Usage

1. (Optional) If you need to pass any API keys, create a `.env` file in the root of the repository with the required key and value pairs:
   ```env
   COHERE_API_KEY=your_core_api_key
   ```
