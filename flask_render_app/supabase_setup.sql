-- Execute this SQL in your Supabase SQL Editor (Dashboard > SQL Editor)

-- Create the prazos table matching the existing project structure
CREATE TABLE prazos (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    descricao TEXT,
    tipo TEXT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    estado TEXT,
    endereco TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    status TEXT DEFAULT 'pending',
    progress INTEGER DEFAULT 0,
    completion_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security (RLS) for security
ALTER TABLE prazos ENABLE ROW LEVEL SECURITY;

-- Create policy to allow all operations for authenticated users (or public if you want)
-- For simplicity, allowing public access (adjust as needed for security)
CREATE POLICY "Allow all operations for everyone" ON prazos
FOR ALL USING (true);

-- Create the photos storage bucket (if not created via UI)
-- Note: You can create this via the Storage tab in Supabase Dashboard instead
-- INSERT INTO storage.buckets (id, name, public) VALUES ('photos', 'photos', true);
