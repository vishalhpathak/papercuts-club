# Papercuts Book Club Website

A modern, community-driven website for the Papercuts book club - 18 members strong and reading together since 2023.

## 🎯 Project Vision

Transform our book club from Google Sheets and manual coordination into a beautiful, engaging web platform that enhances our reading community experience.

## ✅ What We've Built So Far

### Core Infrastructure
- **Next.js 15** with TypeScript and Tailwind CSS
- **Organized project structure** with proper component separation
- **Responsive design** with beautiful gradients and book-themed styling
- **Clean component architecture** (UI components, layouts, pages)

### Current Features
- **Beautiful Homepage** with gradient design and club stats
- **Header/Footer Layout** with Papercuts branding
- **Responsive Design** that works on all devices
- **Component Library** (Button, Card, Header, Footer)

### Database Design (Ready to Implement)
- **Supabase Backend** with PostgreSQL
- **Complete Schema** for all planned features:
  - User profiles with Goodreads integration
  - Book submissions and ratings
  - Meeting management with RSVP
  - Discussion threads
  - Photo galleries
  - Reading progress tracking

## 🚀 Planned Features

### Phase 1: Core Functionality
- [ ] **Authentication System**
  - Google OAuth sign-in
  - Member profiles with bio and reading preferences
  - Goodreads profile linking

- [ ] **Book Management**
  - Annual book submission system (randomized selection)
  - Book details with cover images
  - Member ratings and mini-reviews
  - Reading progress tracking

### Phase 2: Community Features
- [ ] **Meeting Management**
  - Interactive calendar (first Monday of each month)
  - Host selection and location updates
  - RSVP system with status tracking
  - Meeting photo galleries

- [ ] **Discussion Platform**
  - Book-specific discussion threads
  - Member-only conversations
  - Spoiler-safe discussions

### Phase 3: Enhanced Experience
- [ ] **Member Directory**
  - Searchable member profiles
  - Reading history and preferences
  - Member book recommendations

- [ ] **Goodreads Integration**
  - Import member reading lists
  - Sync reading progress
  - Display member reviews
  - Suggest future book picks based on member preferences

### Phase 4: Advanced Features
- [ ] **Reading Challenges**
  - Annual page goals
  - Genre diversity tracking
  - Club reading streaks

- [ ] **Enhanced Social Features**
  - Quote of the month submissions
  - Virtual bookshelf tours
  - Member spotlights
  - Reading anniversary celebrations

## 🛠 Tech Stack

- **Frontend**: Next.js 15, React, TypeScript
- **Styling**: Tailwind CSS with custom gradients
- **Backend**: Supabase (PostgreSQL + Auth + Real-time)
- **Icons**: Lucide React
- **Hosting**: Vercel (planned)
- **Domain**: papercuts.org

## 📁 Project Structure

```
src/
├── app/                     # Next.js App Router pages
├── components/
│   ├── ui/                  # Reusable UI components (Button, Card)
│   ├── layout/              # Layout components (Header, Footer)
│   ├── books/               # Book-specific components
│   ├── meetings/            # Meeting management components
│   └── members/             # Member-related components
├── lib/                     # Utilities and configurations
├── hooks/                   # Custom React hooks
└── types/                   # TypeScript definitions
```

## 🎨 Design Philosophy

- **Book-themed aesthetics** with warm orange/red gradients
- **Community-first approach** - features that bring members together
- **Mobile-responsive** for on-the-go book club management
- **Clean, modern UI** that feels welcoming and literary

## 📋 Current Status

**✅ Completed:**
- Project scaffolding and architecture
- Beautiful homepage design
- Component library foundation
- Database schema design

**🔄 In Progress:**
- Deployment setup (GitHub → Vercel → papercuts.org)

**📝 Next Steps:**
1. Complete deployment pipeline
2. Set up Supabase database
3. Implement authentication system
4. Build book submission feature

## 🤝 How It Replaces Current Workflow

**Before:**
- Google Sheets for book submissions
- Manual calendar invite updates
- Email coordination for meetings
- No central place for discussions

**After:**
- Integrated book submission with voting
- Automated meeting management
- Rich discussion platform
- Member profiles and reading tracking
- Photo galleries and community features

## 🌟 Why This Matters

This isn't just a website - it's about strengthening our book club community. By creating a dedicated space for Papercuts, we're:
- Making it easier to participate and stay engaged
- Creating a lasting archive of our reading journey
- Building deeper connections between members
- Enhancing the joy of reading together

---

*Building community one page at a time* 📚