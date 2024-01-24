import React from "react";
import axios from "axios";
import SEO from "../components/SEO";

export default function Home() {
  function handleSubmit(event) {
    event.preventDefault();
    const text = (document.querySelector("#char-input") as HTMLInputElement).value;

    axios
      .get(`/char_count/?text=${text}`)
      .then(({ data }) => {
        (document.querySelector(
          "#char-count"
        ) as HTMLInputElement).textContent = `${data.count} characters!`;
      })
      .catch((err) => console.log(err));
  }

  return (
    <div>
      <SEO
        title="Frontend"
        description="A starter template for building Next.js + Django RF + Docker web apps."
      />
      <main id="top" className='flex flex-col justify-center items-center h-screen w-screen bg-gray-800 text-white text-2xl space-y-12'>
        <img src="/images/logo.svg" className="h-96" alt="logo" />
        <p>
          Edit <code>pages/index.tsx</code> and save to reload.
        </p>
        <div>
          <label htmlFor="char-input">How many characters does </label>
          <input id="char-input" type="text" placeholder="my string" className="text-black text-center" />
          <button className='button' onClick={handleSubmit}>have?</button>
        </div>
        <div className="text-4xl" id="char-count">
          {" "}
        </div>
      </main>
    </div>
  );
}
