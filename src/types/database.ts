// Database type definitions
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

// More types to be added as features develop
