// Meetings data hook  
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
