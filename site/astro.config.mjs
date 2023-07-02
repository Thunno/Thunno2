// @ts-check

import { defineConfig } from "astro/config";

import tailwind from "@astrojs/tailwind";
import rehypeMathJaxSvg from "rehype-mathjax";
import remarkMath from "remark-math";
import remarkGfm from "remark-gfm";

// https://astro.build/config
export default defineConfig({
  site: "https://thunno.github.io",
  base: "/thunno2",
  integrations: [tailwind()],
  markdown: {
    remarkPlugins: [remarkMath, remarkGfm],
    rehypePlugins: [rehypeMathJaxSvg],
  },
  vite: {
    resolve: {
      preserveSymlinks: true,
    },
  },
});
