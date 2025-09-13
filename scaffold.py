#!/usr/bin/env python3
"""
Papercuts Book Club - Project Scaffolding Script
Creates the complete folder structure and placeholder files for organized development
"""

import os
import sys

def create_directory(path):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✓ Created directory: {path}")
    except Exception as e:
        print(f"✗ Failed to create {path}: {e}")

def create_file(path, content=""):
    """Create file with optional content"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created file: {path}")
    except Exception as e:
        print(f"✗ Failed to create {path}: {e}")

def scaffold_papercuts():
    """Main scaffolding function"""
    print("🚀 Scaffolding Papercuts Book Club project structure...\n")
    
    # Base directories under src/
    directories = [
        "src/components/ui",
        "src/components/layout", 
        "src/components/books",
        "src/components/meetings",
        "src/components/members",
        "src/lib",
        "src/hooks", 
        "src/types",
        "src/app/auth/callback",
        "src/app/books/submit",
        "src/app/books/[id]",
        "src/app/members/[id]",
        "src/app/meetings/[id]",
        "src/app/profile"
    ]
    
    # Create all directories
    print("📁 Creating directories...")
    for directory in directories:
        create_directory(directory)
    
    print("\n📄 Creating core files...")
    
    # Core library files
    lib_files = {
        "src/lib/supabase.ts": '''// Supabase client configuration and types
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

// Database types will be defined here
export type Profile = {
  id: string
  email: string
  display_name: string | null
  // More fields to be added
}

// More types to be added as we build features
''',
        
        "src/lib/auth.ts": '''// Authentication utilities
import { supabase } from './supabase'

export const signInWithGoogle = async () => {
  const { error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: `${window.location.origin}/auth/callback`
    }
  })
  return { error }
}

export const signOut = async () => {
  const { error } = await supabase.auth.signOut()
  return { error }
}
''',
        
        "src/lib/database.ts": '''// Database query functions
import { supabase } from './supabase'

// Book-related queries
export const getBooks = async () => {
  const { data, error } = await supabase
    .from('books')
    .select('*')
    .order('created_at', { ascending: false })
  
  return { data, error }
}

// Meeting-related queries  
export const getMeetings = async () => {
  const { data, error } = await supabase
    .from('meetings')
    .select('*, book:books(*), host:profiles(*)')
    .order('meeting_date', { ascending: true })
  
  return { data, error }
}

// More query functions to be added
''',
        
        "src/lib/utils.ts": '''// General utility functions
import { clsx, type ClassValue } from "clsx"

export function cn(...inputs: ClassValue[]) {
  return clsx(inputs)
}

export const formatDate = (date: string | Date) => {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long', 
    day: 'numeric'
  })
}
'''
    }
    
    # Hook files
    hook_files = {
        "src/hooks/useAuth.ts": '''// Authentication hook
import { useState, useEffect } from 'react'
import { supabase } from '@/lib/supabase'
import type { User } from '@supabase/supabase-js'

export const useAuth = () => {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Get initial session
    supabase.auth.getUser().then(({ data }) => {
      setUser(data.user)
      setLoading(false)
    })

    // Listen for auth changes
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      setUser(session?.user || null)
      setLoading(false)
    })

    return () => subscription.unsubscribe()
  }, [])

  return { user, loading }
}
''',
        
        "src/hooks/useBooks.ts": '''// Books data hook
import { useState, useEffect } from 'react'
import { getBooks } from '@/lib/database'

export const useBooks = () => {
  const [books, setBooks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchBooks = async () => {
      const { data, error } = await getBooks()
      if (error) {
        setError(error.message)
      } else {
        setBooks(data || [])
      }
      setLoading(false)
    }

    fetchBooks()
  }, [])

  return { books, loading, error, refetch: () => setLoading(true) }
}
''',
        
        "src/hooks/useMeetings.ts": '''// Meetings data hook  
import { useState, useEffect } from 'react'
import { getMeetings } from '@/lib/database'

export const useMeetings = () => {
  const [meetings, setMeetings] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchMeetings = async () => {
      const { data, error } = await getMeetings()
      if (error) {
        setError(error.message)
      } else {
        setMeetings(data || [])
      }
      setLoading(false)
    }

    fetchMeetings()
  }, [])

  return { meetings, loading, error, refetch: () => setLoading(true) }
}
'''
    }
    
    # Type definition files
    type_files = {
        "src/types/database.ts": '''// Database type definitions
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
''',
        
        "src/types/index.ts": '''// Export all types
export * from './database'
'''
    }
    
    # UI Component files
    ui_files = {
        "src/components/ui/Button.tsx": '''// Reusable Button component
import { cn } from '@/lib/utils'

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline'
  size?: 'sm' | 'md' | 'lg'
}

export const Button = ({ 
  className, 
  variant = 'primary', 
  size = 'md', 
  ...props 
}: ButtonProps) => {
  return (
    <button
      className={cn(
        'rounded-lg font-medium transition-colors',
        {
          'bg-orange-500 hover:bg-orange-600 text-white': variant === 'primary',
          'bg-gray-100 hover:bg-gray-200 text-gray-900': variant === 'secondary',
          'border border-gray-300 hover:bg-gray-50': variant === 'outline',
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-4 py-2': size === 'md', 
          'px-6 py-3 text-lg': size === 'lg'
        },
        className
      )}
      {...props}
    />
  )
}
''',
        
        "src/components/ui/Card.tsx": '''// Reusable Card component
import { cn } from '@/lib/utils'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode
}

export const Card = ({ className, children, ...props }: CardProps) => {
  return (
    <div 
      className={cn(
        'bg-white rounded-lg shadow-md border border-gray-200 p-6',
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}
'''
    }
    
    # Layout components
    layout_files = {
        "src/components/layout/Header.tsx": '''// Main site header
'use client'

import { useAuth } from '@/hooks/useAuth'
import { signInWithGoogle, signOut } from '@/lib/auth'
import { BookOpen } from 'lucide-react'
import { Button } from '@/components/ui/Button'

export const Header = () => {
  const { user, loading } = useAuth()

  const handleSignIn = async () => {
    const { error } = await signInWithGoogle()
    if (error) console.error('Sign in error:', error)
  }

  const handleSignOut = async () => {
    const { error } = await signOut()
    if (error) console.error('Sign out error:', error)
  }

  if (loading) return <div>Loading...</div>

  return (
    <header className="bg-white shadow-sm border-b">
      <div className="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
        <div className="flex items-center space-x-3">
          <BookOpen className="w-8 h-8 text-orange-500" />
          <div>
            <h1 className="text-xl font-bold text-gray-900">Papercuts</h1>
            <p className="text-sm text-gray-600">Book Club</p>
          </div>
        </div>
        
        <div>
          {user ? (
            <div className="flex items-center space-x-4">
              <span>Welcome back!</span>
              <Button variant="secondary" onClick={handleSignOut}>
                Sign Out
              </Button>
            </div>
          ) : (
            <Button onClick={handleSignIn}>
              Sign In
            </Button>
          )}
        </div>
      </div>
    </header>
  )
}
''',
        
        "src/components/layout/Footer.tsx": '''// Site footer
import { BookOpen } from 'lucide-react'

export const Footer = () => {
  return (
    <footer className="bg-gray-50 border-t py-8">
      <div className="max-w-6xl mx-auto px-4 text-center">
        <div className="flex items-center justify-center space-x-2 mb-4">
          <BookOpen className="w-5 h-5 text-orange-500" />
          <span className="font-semibold text-gray-900">Papercuts Book Club</span>
        </div>
        <p className="text-gray-600">
          Building community one page at a time • Est. 2023
        </p>
      </div>
    </footer>
  )
}
'''
    }
    
    # App route files
    app_files = {
        "src/app/auth/callback/route.ts": '''// Auth callback route
import { createRouteHandlerClient } from '@supabase/auth-helpers-nextjs'
import { cookies } from 'next/headers'
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const requestUrl = new URL(request.url)
  const code = requestUrl.searchParams.get('code')

  if (code) {
    const cookieStore = cookies()
    const supabase = createRouteHandlerClient({ cookies: () => cookieStore })
    await supabase.auth.exchangeCodeForSession(code)
  }

  return NextResponse.redirect(requestUrl.origin)
}
''',
        
        ".env.local": '''# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url_here
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key_here
'''
    }
    
    # Create all files
    all_files = {**lib_files, **hook_files, **type_files, **ui_files, **layout_files, **app_files}
    
    for file_path, content in all_files.items():
        create_file(file_path, content)
    
    print(f"\n🎉 Successfully scaffolded Papercuts project!")
    print(f"📊 Created {len(directories)} directories and {len(all_files)} files")
    print("\n📋 Next steps:")
    print("1. Install additional dependencies: npm install @supabase/supabase-js @supabase/auth-helpers-nextjs lucide-react date-fns clsx")
    print("2. Set up Supabase project and update .env.local")
    print("3. Start development server: npm run dev")
    print("\n✨ Happy coding!")

if __name__ == "__main__":
    # Check if we're in the right directory
    if not os.path.exists("package.json"):
        print("❌ Error: This doesn't appear to be a Next.js project directory.")
        print("Please run this script from your papercuts project root (where package.json exists)")
        sys.exit(1)
    
    scaffold_papercuts()