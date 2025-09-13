// Database query functions
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
