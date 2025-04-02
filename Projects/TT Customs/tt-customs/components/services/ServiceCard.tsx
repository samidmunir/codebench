'use client'

import { motion } from 'framer-motion'

interface ServiceCardProps {
  title: string
  description: string
  cost: number
  timeEstimate: string
  dropOffRequired: boolean
  isSelected: boolean
  onToggle: () => void
}

const ServiceCard = ({
  title,
  description,
  cost,
  timeEstimate,
  dropOffRequired,
  isSelected,
  onToggle
}: ServiceCardProps) => {
  return (
    <motion.div
      layout
      className={`bg-zinc-800 text-zinc-200 rounded-lg p-6 border transition cursor-pointer ${
        isSelected ? 'border-red-500 shadow-lg shadow-red-500/20' : 'border-zinc-700 hover:border-red-500'
      }`}
      onClick={onToggle}
    >
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-2xl font-semibold text-red-500">{title}</h3>
        <input
          type="checkbox"
          checked={isSelected}
          onChange={() => {}}
          className="accent-red-500 w-5 h-5 pointer-events-none"
        />
      </div>
      <p className="text-sm text-zinc-400 mb-4">{description}</p>
      <ul className="text-sm text-zinc-300 mb-4 space-y-1">
        <li><strong>Cost:</strong> ${cost.toFixed(2)}</li>
        <li><strong>Estimated Time:</strong> {timeEstimate}</li>
        <li><strong>Drop-Off Required:</strong> {dropOffRequired ? 'Yes' : 'No'}</li>
      </ul>
    </motion.div>
  )
}

export default ServiceCard
