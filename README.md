# Lipari school: A deep dive into Weaviate - example notebooks

## Resources

- A GitHub account (sign up [here](https://github.com/signup))
- A Weaviate Cloud account (sign up [here](https://console.weaviate.cloud/))
- Some notebooks will use Cohere for embeddings and Anthropic for generative AI. If you would like to follow these, you need to sign up for an account, and the usage in the notebooks will incur a small cost.

## Environment setup

### Using GitHub Codespaces

1. Click on the green "Code" button in the top right corner of the repository
2. Select "Open with Codespaces"
3. Click on "New codespace"
4. Wait for the codespace to build and start

> Note: This should have set up a Python environment, and activated it for you.
>
> If the line you see in the shell does NOT start with `(202507-lipari-school)`,
> make sure the setup is finished (wait a few more minutes) or try opening a new shell.

### Local setup

Use the following steps to set up your local environment:

1. Clone the repository:
   ```bash
   git clone git@github.com:weaviate-tutorials/202507-lipari-school.git
   ```
2. Change into the directory:
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```
5. Edit the `.env` file with your Weaviate Cloud details:
6. Activate the Python environment:
   ```bash
   source .venv/bin/activate
   ```

## Setting up Weaviate Cloud

### Step 1: Create a Weaviate Cloud Instance

1. Go to the [Weaviate Cloud Console](https://console.weaviate.cloud/) and create a new Weaviate instance
2. The Sandbox tier is free and perfect for learning
3. Once your instance is created, note down the URL and API key

### Step 2: Configure Your Environment

1. The CodeSpace set up will have created a `.env` file created for you
   (If not, create it with `cp .env.example .env`.)

2. Edit the `.env` file with your Weaviate Cloud details:
   ```env
   # Your Weaviate Cloud instance URL
   # Example: d4vzkuatq9cfkil33yifwq.c0.europe-west3.gcp.weaviate.cloud
   WEAVIATE_URL=your-cluster-url-here

   # Your Weaviate Cloud API key
   # Create an "admin" key and get it from your Weaviate Cloud Console
   WEAVIATE_API_KEY=your-api-key-here
   ```

### Check that you can run scripts & run

```shell
python try_this.py
```

## Notebooks

The notebooks are named in order of the topics they cover. Please explore them in their order.

## Documentation

For additional information, please refer to the [Weaviate documentation](https://docs.weaviate.io/weaviate).
