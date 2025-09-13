// Authentication utilities
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
