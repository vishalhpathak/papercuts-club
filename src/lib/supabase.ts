@"
// src/lib/supabase.ts
import { createBrowserClient } from '@supabase/ssr'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!

export const supabase = createBrowserClient(supabaseUrl, supabaseAnonKey)

// Database types
export interface Profile {
  id: string
  email: string
  display_name: string | null
  bio: string | null
  favorite_genres: string[] | null
  goodreads_profile: string | null
  avatar_url: string | null
  created_at: string
  updated_at: string
}

export interface Book {
  id: string
  title: string
  author: string
  isbn: string | null
  description: string | null
  cover_url: string | null
  goodreads_url: string | null
  submitted_by: string | null
  submission_year: number
  reading_month: number | null
  created_at: string
}

export interface Meeting {
  id: string
  book_id: string | null
  meeting_date: string
  location: string | null
  location_details: string | null
  host_id: string | null
  created_at: string
  updated_at: string
  book?: Book
  host?: Profile
}
"@ | Out-File -FilePath "src/lib/supabase.ts" -Encoding UTF8