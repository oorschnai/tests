import Fastify from "npm:fastify@5.6.1";

const app = Fastify({ logger: true });
const port = Number(Deno.env.get("PORT") ?? "3000");

app.get("/", async () => {
  return { message: "Timeweb Cloud + Fastify on Deno" };
});

await app.listen({
  port,
  host: "0.0.0.0",
});
