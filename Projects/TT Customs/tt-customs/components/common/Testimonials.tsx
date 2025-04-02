'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'

const testimonials = [
  {
    name: 'Ali R.',
    item: 'Ambient Lighting Installation',
    feedback: 'Absolutely stunning upgrade! My car looks luxurious inside and the team was super professional.',
  },
  {
    name: 'Sana A.',
    item: 'Virtual Dash Upgrade',
    feedback: 'Feels like I’m driving a brand new BMW. Installation was smooth and quick!',
  },
  {
    name: 'Usman Q.',
    item: 'Starlight Roof Installation',
    feedback: 'This is the best investment I’ve made in my car. Everyone who rides with me is amazed.',
  },
  {
    name: 'Zara M.',
    item: 'Custom LED Headlights',
    feedback: 'Clean install and absolutely love the futuristic look. 10/10 experience!',
  },
]

const Testimonials = () => {
  const [current, setCurrent] = useState(0)

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrent((prev) => (prev + 1) % testimonials.length)
    }, 6000) // 6 seconds per slide

    return () => clearInterval(interval)
  }, [])

  const testimonial = testimonials[current]

  return (
    <div className="w-full bg-zinc-900 text-white py-16 px-6 flex flex-col items-center border-t border-red-500">
      <h2 className="text-3xl font-bold text-red-500 mb-8 text-center">What Our Customers Say</h2>

      <div className="max-w-2xl w-full relative overflow-hidden">
        <AnimatePresence mode="wait">
          <motion.div
            key={testimonial.name}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.5 }}
            className="bg-zinc-800 p-6 rounded-lg border border-zinc-700 shadow-md"
          >
            <p className="text-zinc-300 text-sm mb-4">&ldquo;{testimonial.feedback}&rdquo;</p>
            <div className="text-sm text-zinc-400">
              — <span className="text-white font-medium">{testimonial.name}</span>, {testimonial.item}
            </div>
          </motion.div>
        </AnimatePresence>
      </div>

      <div className="flex gap-2 mt-6">
        {testimonials.map((_, idx) => (
          <button
            key={idx}
            onClick={() => setCurrent(idx)}
            className={`w-3 h-3 rounded-full ${
              idx === current ? 'bg-red-500' : 'bg-zinc-600'
            } transition`}
          />
        ))}
      </div>
    </div>
  )
}

export default Testimonials