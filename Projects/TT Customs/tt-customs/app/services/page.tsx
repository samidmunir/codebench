'use client'

import { useState } from 'react'
import ServiceCard from '@/components/services/ServiceCard'
import BookingModal from '@/components/services/BookingModal'

const sampleServices = [
  {
    title: 'Ambient Lighting Installation',
    description: 'Upgrade your vehicle with stunning ambient lighting. Fully customizable and professionally installed.',
    cost: 375.0,
    timeEstimate: '2–3 hours',
    dropOffRequired: true,
  },
  {
    title: 'Starlight Roof Installation',
    description: 'Install a premium starlight ceiling with a sleek, luxury finish.',
    cost: 250.0,
    timeEstimate: '5–6 hours',
    dropOffRequired: true,
  },
  {
    title: 'Virtual Dash Upgrade (BMW)',
    description: 'Modernize your dashboard with a virtual display — compatible with select BMW models.',
    cost: 400.0,
    timeEstimate: '1.5–2 hours',
    dropOffRequired: false,
  },
]

// Dummy available slots
const availableSlots = {
  '2025-04-03': ['10:00 AM', '11:00 AM', '1:00 PM'],
  '2025-04-04': ['9:00 AM', '12:00 PM'],
  '2025-04-05': ['10:30 AM', '2:00 PM'],
}

const ServicesPage = () => {
  const [selected, setSelected] = useState<string[]>([])
  const [showModal, setShowModal] = useState(false)
  const [confirmedBooking, setConfirmedBooking] = useState<{ date: string; time: string } | null>(null)

  const toggleService = (title: string) => {
    setSelected(prev =>
      prev.includes(title) ? prev.filter(s => s !== title) : [...prev, title]
    )
  }

  const selectedServices = sampleServices.filter(service =>
    selected.includes(service.title)
  )

  const totalCost = selectedServices.reduce((sum, s) => sum + s.cost, 0)
  const totalTime = selectedServices.map(s => s.timeEstimate).join(' + ')

  const handleBookingClick = () => {
    setShowModal(true)
  }

  const handleBookingConfirm = (date: string, time: string, name: string, email: string) => {
    setConfirmedBooking({ date, time })
    setShowModal(false)
    setSelected([])
  }

  return (
    <div className="min-h-screen px-6 py-16 bg-zinc-900 text-white">
      <h1 className="text-4xl font-bold text-red-500 mb-8 text-center">Our Services</h1>

      <div className="flex flex-col lg:flex-row gap-8 items-start">
        {/* Service Cards */}
        <div className="w-full lg:flex-1 grid gap-8 md:grid-cols-2 xl:grid-cols-3">
          {sampleServices.map(service => (
            <ServiceCard
              key={service.title}
              {...service}
              isSelected={selected.includes(service.title)}
              onToggle={() => toggleService(service.title)}
            />
          ))}
        </div>

        {/* Sidebar */}
        <aside className="w-full lg:w-80 shrink-0 bg-zinc-800 border border-zinc-700 p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold text-red-500 mb-4">Selected Services</h2>

          {selectedServices.length === 0 ? (
            <p className="text-zinc-400 text-sm">No services selected yet.</p>
          ) : (
            <ul className="mb-4 space-y-2 text-sm text-zinc-300">
              {selectedServices.map(s => (
                <li key={s.title} className="flex justify-between border-b border-zinc-700 pb-1">
                  <span>{s.title}</span>
                  <span>${s.cost.toFixed(2)}</span>
                </li>
              ))}
            </ul>
          )}

          <p className="text-zinc-200 font-medium text-sm">
            Total: <span className="text-red-500">${totalCost.toFixed(2)}</span>
          </p>

          {selectedServices.length > 0 && (
            <button
              onClick={handleBookingClick}
              className="mt-4 w-full bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm transition"
            >
              Book Selected Services
            </button>
          )}
        </aside>
      </div>

      {showModal && (
        <BookingModal
          services={selected}
          onClose={() => setShowModal(false)}
          onConfirm={handleBookingConfirm}
          availableSlots={availableSlots}
          summary={{ cost: totalCost, time: totalTime }}
        />
      )}

      {confirmedBooking && (
        <div className="mt-8 text-center text-zinc-300">
          Booking confirmed for{' '}
          <span className="text-red-500">{confirmedBooking.date}</span> at{' '}
          <span className="text-red-500">{confirmedBooking.time}</span>!
        </div>
      )}
    </div>
  )
}

export default ServicesPage
