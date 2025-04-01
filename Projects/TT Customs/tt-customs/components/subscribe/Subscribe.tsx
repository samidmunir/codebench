// components/subscribe/Subscribe.tsx

'use client'

const Subscribe = () => {
  return (
    <section className="bg-zinc-900 px-6 py-16 text-center text-zinc-200 border-t border-b border-red-500">
      <div className="max-w-2xl mx-auto">
        <h2 className="text-4xl font-bold text-red-500 mb-4">Join the TT Customs Family</h2>
        <p className="text-zinc-400 mb-8">
          Get updates on the latest gear, exclusive deals, and priority booking access.
        </p>

        <form className="flex flex-col sm:flex-row gap-4 justify-center">
          <input
            type="email"
            required
            placeholder="Enter your email"
            className="px-4 py-3 rounded-md bg-zinc-800 text-white border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-red-500 w-full sm:w-auto"
          />
          <button
            type="submit"
            className="bg-red-500 hover:bg-red-600 transition px-6 py-3 rounded-md text-white font-semibold"
          >
            Subscribe
          </button>
        </form>

        <p className="text-xs text-zinc-500 mt-4">
          No spam. Just quality updates and exclusive offers.
        </p>
      </div>
    </section>
  );
};

export default Subscribe;