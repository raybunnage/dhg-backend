# FastAPI Supabase Backend

## Setup
1. Copy `.env.example` to `.env`
2. Update `.env` with your Supabase credentials
3. Create virtual environment: `python -m venv venv`
4. Activate virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run server: `cd backend && python server.py`

## Environment Variables
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase anonymous key