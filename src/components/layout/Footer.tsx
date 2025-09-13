// Site footer
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
