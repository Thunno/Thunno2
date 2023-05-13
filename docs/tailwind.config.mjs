// @ts-check

/** @type {import("tailwindcss").Config} */
const config = {
  content: ["./src/**/*.astro"],
  theme: {
    extend: {
      fontFamily: {
        display: ["Karla", "sans-serif"],
      },
    },
  },
  plugins: [],
};
export default config;
