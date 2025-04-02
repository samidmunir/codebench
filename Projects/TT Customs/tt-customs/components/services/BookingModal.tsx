'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'

interface BookingModalProps {
  services: string[]
  onClose: () => void
  onConfirm: (date: string, time: string, name: string, email: string) => void
  availableSlots: Record<string, string[]>
  summary: { cost: number; time: string }
}

const BookingModal = ({ services, onClose, onConfirm, availableSlots, summary }: BookingModalProps) => {
  const [selectedDate, setSelectedDate] = useState('')
  const [selectedTime, setSelectedTime] = useState('')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')

  const dates = Object.keys(availableSlots)
  const timesForSelectedDate = selectedDate ? availableSlots[selectedDate] : []

  const isFormComplete = name && email && selectedDate && selectedTime

  const handleSubmit = () => {
    if (isFormComplete) {
      onConfirm(selectedDate, selectedTime, name, email)
    }
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex justify-center items-center z-50">
      <motion.div
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ opacity: 0 }}
        className="bg-zinc-900 p-6 rounded-lg max-w-lg w-full border border-red-500 shadow-lg"
      >
        <h2 className="text-2xl font-bold text-red-500 mb-4">Book Services</h2>
        <p className="text-sm text-zinc-300 mb-4">
          Services: <span className="text-white">{services.join(', ')}</span>
        </p>

        {/* Customer Info */}
        <input
          type="text"
          placeholder="Your Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full mb-3 p-2 rounded bg-zinc-800 border border-zinc-700 text-white"
        />
        <input
          type="email"
          placeholder="Your Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full mb-4 p-2 rounded bg-zinc-800 border border-zinc-700 text-white"
        />

        {/* Date Picker */}
        <label className="block mb-2 text-zinc-400">Select a Date:</label>
        <select
          className="w-full mb-4 p-2 rounded bg-zinc-800 border border-zinc-700 text-white"
          value={selectedDate}
          onChange={(e) => {
            setSelectedDate(e.target.value)
            setSelectedTime('')
          }}
        >
          <option value="">-- Choose Date --</option>
          {dates.map((date) => (
            <option key={date} value={date}>{date}</option>
          ))}
        </select>

        {/* Time Slots */}
        {selectedDate && (
          <>
            <label className="block mb-2 text-zinc-400">Available Time Slots:</label>
            <div className="grid grid-cols-2 gap-2 mb-4">
              {timesForSelectedDate.length ? (
                timesForSelectedDate.map((time) => (
                  <button
                    key={time}
                    onClick={() => setSelectedTime(time)}
                    className={`px-4 py-2 rounded border text-sm ${
                      selectedTime === time
                        ? 'bg-red-500 text-white'
                        : 'bg-zinc-800 text-zinc-200 border-zinc-700 hover:border-red-500'
                    }`}
                  >
                    {time}
                  </button>
                ))
              ) : (
                <span className="text-zinc-400 text-sm col-span-2">No available time slots.</span>
              )}
            </div>
          </>
        )}

        {/* Summary */}
        <div className="text-sm text-zinc-400 mb-4 border-t pt-4 border-zinc-700">
          <p><strong>Total Estimated Time:</strong> {summary.time}</p>
          <p><strong>Total Cost:</strong> ${summary.cost.toFixed(2)}</p>
        </div>

        {/* Confirm / Cancel Buttons */}
        <div className="flex justify-end gap-4">
          <button
            onClick={onClose}
            className="text-zinc-400 hover:text-red-400 text-sm transition"
          >
            Cancel
          </button>
          <button
            onClick={handleSubmit}
            disabled={!isFormComplete}
            className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm transition disabled:opacity-50"
          >
            Confirm Booking
          </button>
        </div>
      </motion.div>
    </div>
  )
}

export default BookingModal
