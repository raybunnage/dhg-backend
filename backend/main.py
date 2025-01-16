from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
import os
from pathlib import Path
from dotenv import load_dotenv

print("\n=== Environment Setup Debug ===")
print(f"Current directory: {os.getcwd()}")
print(f"Parent directory: {Path(os.getcwd()).parent}")
print(f".env exists in current dir: {os.path.exists('.env')}")
print(f".env exists in parent dir: {os.path.exists('../.env')}")

# Load environment variables from parent directory
print("\n=== Loading .env file ===")
env_path = Path(os.getcwd()).parent / ".env"
print(f"Looking for .env at: {env_path}")
print(f"File exists: {env_path.exists()}")

load_dotenv(dotenv_path=env_path)

# Debug: Print environment variables
print("\n=== Environment Variables ===")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
print(f"SUPABASE_URL: {supabase_url}")
print(f"SUPABASE_KEY: {supabase_key[:30]}...") if supabase_key else print(
    "SUPABASE_KEY: None"
)

print("\n=== Initializing FastAPI ===")
# Initialize FastAPI app
app = FastAPI(title="FastAPI Supabase Backend")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("\n=== Creating Supabase Client ===")
# Initialize Supabase client
supabase = create_client(supabase_url, supabase_key)
print("Supabase client created successfully")


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with Supabase!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
