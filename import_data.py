import weaviate
from weaviate.classes.config import Property, DataType, Configure, Tokenization
from weaviate.util import generate_uuid5
import os
from tqdm import tqdm
from pathlib import Path
import base64
from dotenv import load_dotenv

load_dotenv(override=True)

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=os.getenv("WEAVIATE_API_KEY"),
    headers={
        "X-Cohere-Api-Key": os.getenv("COHERE_API_KEY"),
        "X-Anthropic-Api-Key": os.getenv("ANTHROPIC_API_KEY"),
    }
)

client.collections.delete("Pages")

client.collections.create(
    name="Pages",
    properties=[
        Property(
            name="document_title",
            data_type=DataType.TEXT,
        ),
        Property(
            name="page_image",
            data_type=DataType.BLOB,
        ),
        Property(
            name="filename",
            data_type=DataType.TEXT,
            tokenization=Tokenization.FIELD
        ),
    ],
    vector_config=[
        # Add `Configure.Vectors.multi2vec_cohere` vector to the collection with:
        # name: "default", source properties: ["page_image"], and model: "embed-v4.0"
        Configure.Vectors.multi2vec_cohere(
            name="default",
            image_fields=["page_image"],
            model="embed-v4.0"
        )
    ]
)

pages = client.collections.get("Pages")

img_paths = sorted(list(Path("data/imgs").glob("hai_ai*.jpg")))
print(f"importing {len(img_paths)} files...")

with pages.batch.fixed_size(batch_size=10) as batch:
    for i, filepath in tqdm(enumerate(img_paths)):
        print(f"Processing {filepath}")
        image = filepath.read_bytes()
        base64_image = base64.b64encode(image).decode('utf-8')
        obj = {
            "document_title": "HAI AI Index report 2025",
            "page_image": base64_image,
            "filename": filepath.name
        }

        # Add object to batch for import with (batch.add_object())
        batch.add_object(
            properties=obj,
            uuid=generate_uuid5(str(filepath))
        )

print(len(pages))

client.close()
