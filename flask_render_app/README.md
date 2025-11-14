# Flask Render App - FlexMap Backend

A Flask API deployed on Render with shared project data using Supabase, replacing the local TiDB storage.

## Setup

1. Create a Supabase project at https://supabase.com
2. Run the SQL in `supabase_setup.sql` in your Supabase SQL Editor to create the `prazos` table
3. Copy `.env.example` to `.env` and fill in your Supabase URL and anon key
4. Run locally: `pip install -r requirements.txt` then `python app.py`

## Deploy to Render

1. Create a GitHub repository and push this code
2. Go to Render.com and create a new Web Service
3. Connect your GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Add environment variables: SUPABASE_URL and SUPABASE_KEY
7. Deploy

## API Endpoints

- `GET /api/prazos` - Get all projects
- `POST /api/prazos` - Create new project
- `PUT /api/prazos/<id>` - Update project
- `DELETE /api/prazos/<id>` - Delete project

## Features

- Shared project data across all users
- Data persists permanently in Supabase
- Compatible with existing FlexMap frontend
- CORS enabled for cross-origin requests
