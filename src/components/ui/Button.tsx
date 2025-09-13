// Reusable Button component
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
