// @ts-check
import typography from "@tailwindcss/typography";

/** @type {import("tailwindcss").Config} */
const config = {
  content: ["./src/**/*.astro"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Seravek", "sans-serif"],
      },
    },
  },
  plugins: [typography],
};
export default config;
