// Books data hook
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
