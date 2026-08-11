import Hapi from "npm:@hapi/hapi@21.4.3";

const port = Number(Deno.env.get("PORT") ?? "3000");

const server = Hapi.server({
  port,
  host: "0.0.0.0",
});

server.route({
  method: "GET",
  path: "/",
  handler: () => "Timeweb Cloud + Hapi on Deno",
});

await server.start();
console.log("Hapi server is running on " + server.info.uri);
