import typography from "@tailwindcss/typography";

// @ts-check

/** @type {import("tailwindcss").Config} */
const config = {
  content: ["./src/**/*.astro"],
  theme: {
    extend: {
      fontFamily: {
        // display: ["Karla", "sans-serif"],
        sans: ["Seravek", "sans-serif"],
      },
    },
  },
  plugins: [typography],
};
export default config;
