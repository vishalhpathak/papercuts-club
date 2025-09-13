// Reusable Card component
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
