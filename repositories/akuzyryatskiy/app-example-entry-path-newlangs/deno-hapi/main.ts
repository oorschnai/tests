import Hapi from "@hapi/hapi";

const port = Number(Deno.env.get("PORT") ?? "8000");

const server = Hapi.server({
  port,
  host: "0.0.0.0",
});

server.route({
  method: "GET",
  path: "/",
  handler: () => "Timeweb Cloud + Deno Hapi",
});

server.route({
  method: "GET",
  path: "/health",
  handler: () => ({ status: "ok" }),
});

await server.start();
console.log(`Listening on ${server.info.uri}`);