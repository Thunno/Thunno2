import { z, defineCollection } from "astro:content";
const docsCollection = defineCollection({
  schema: z.object({
    title: z.string(),
    ignore: z.boolean().default(false),
  }),
});
export const collections = {
  docs: docsCollection,
};
