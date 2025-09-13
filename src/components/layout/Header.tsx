// src/components/layout/Header.tsx
'use client'

import { BookOpen } from 'lucide-react'
import { Button } from '@/components/ui/Button'

export const Header = () => {
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
          <Button variant="secondary">
            Sign In (Coming Soon)
          </Button>
        </div>
      </div>
    </header>
  )
}