'use client'

import { usePathname } from 'next/navigation'
import { useEffect, useState } from 'react'
import LoadingSpinner from './ui/LoadingSpinner'

const RouteChangeIndicator = () => {
  const pathname = usePathname()
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    // Show spinner immediately
    setLoading(true)

    // Ensure it's visible for at least 1 second
    const timeout = setTimeout(() => {
      setLoading(false)
    }, 1000)

    return () => clearTimeout(timeout)
  }, [pathname])

  return loading ? <LoadingSpinner /> : null
}

export default RouteChangeIndicator
