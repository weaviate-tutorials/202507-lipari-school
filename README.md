# Lipari school: A deep dive into Weaviate

## Student prerequisites

- A GitHub account (sign up [here](https://github.com/signup))
- A Weaviate Cloud account (sign up [here](https://console.weaviate.cloud/))

### Github Codespaces

1. Click on the green "Code" button in the top right corner of the repository
2. Select "Open with Codespaces"
3. Click on "New codespace"
4. Wait for the codespace to build and start

## Setting up Weaviate Cloud

### Step 1: Create a Weaviate Cloud Instance

1. Go to the [Weaviate Cloud Console](https://console.weaviate.cloud/) and create a new Weaviate instance
2. The Sandbox tier is free and perfect for learning
3. Once your instance is created, note down the URL and API key

### Step 2: Configure Your Environment

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your Weaviate Cloud details:
   ```env
   WEAVIATE_URL=https://your-cluster-name.weaviate.network
   WEAVIATE_API_KEY=your-api-key-here
   ```
