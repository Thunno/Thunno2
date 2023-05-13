import { defineConfig } from "astro/config";

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  site: "https://thunno.github.io",
  base: "/thunno2",
  integrations: [tailwind()]
});