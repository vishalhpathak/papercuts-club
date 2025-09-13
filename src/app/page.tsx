'use client'

import { Header } from '@/components/layout/Header'
import { Footer } from '@/components/layout/Footer'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { BookOpen, Users, Calendar } from 'lucide-react'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-50 via-orange-50 to-red-50">
      <Header />
      
      <main className="max-w-6xl mx-auto px-4 py-12">
        {/* Hero Section */}
        <section className="text-center mb-16">
          <h1 className="text-6xl font-bold text-gray-900 mb-6">
            Welcome to <span className="bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent">Papercuts</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Our cozy book club where stories come alive and friendships are bound by pages. 
            Meeting monthly since 2023.
          </p>
          
          <div className="flex flex-wrap justify-center gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full flex items-center justify-center mx-auto mb-3">
                <Users className="w-8 h-8 text-white" />
              </div>
              <h3 className="font-bold text-lg text-gray-900">18 Members</h3>
              <p className="text-gray-600">Active readers</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-br from-green-400 to-blue-500 rounded-full flex items-center justify-center mx-auto mb-3">
                <BookOpen className="w-8 h-8 text-white" />
              </div>
              <h3 className="font-bold text-lg text-gray-900">2+ Years</h3>
              <p className="text-gray-600">Reading together</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-br from-purple-400 to-pink-500 rounded-full flex items-center justify-center mx-auto mb-3">
                <Calendar className="w-8 h-8 text-white" />
              </div>
              <h3 className="font-bold text-lg text-gray-900">Monthly</h3>
              <p className="text-gray-600">First Mondays</p>
            </div>
          </div>
        </section>

        {/* Feature Cards */}
        <section className="grid md:grid-cols-3 gap-8 mb-16">
          <Card className="text-center hover:shadow-lg transition-shadow">
            <BookOpen className="w-12 h-12 text-orange-500 mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-3">Submit Books</h3>
            <p className="text-gray-600 mb-4">
              Suggest your favorite reads for the club to discover together.
            </p>
            <Button variant="outline" className="w-full">
              Coming Soon
            </Button>
          </Card>

          <Card className="text-center hover:shadow-lg transition-shadow">
            <Users className="w-12 h-12 text-blue-500 mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-3">Meet Members</h3>
            <p className="text-gray-600 mb-4">
              Connect with fellow book lovers and discover reading recommendations.
            </p>
            <Button variant="outline" className="w-full">
              Coming Soon
            </Button>
          </Card>

          <Card className="text-center hover:shadow-lg transition-shadow">
            <Calendar className="w-12 h-12 text-purple-500 mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-3">Track Meetings</h3>
            <p className="text-gray-600 mb-4">
              Never miss a meeting with our interactive calendar and RSVP system.
            </p>
            <Button variant="outline" className="w-full">
              Coming Soon
            </Button>
          </Card>
        </section>

        {/* Call to Action */}
        <section className="text-center">
          <Card className="max-w-2xl mx-auto">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Ready to join the conversation?
            </h2>
            <p className="text-gray-600 mb-6">
              Sign in to access member features, submit books, and connect with your reading community.
            </p>
            <Button size="lg" className="bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-600 hover:to-red-600">
              Sign In to Get Started
            </Button>
          </Card>
        </section>
      </main>

      <Footer />
    </div>
  )
}
