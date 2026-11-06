import express from "express";

const app = express();
const port = Number.parseInt(Deno.env.get("DENO_PORT") ?? "3001", 10);

app.get("/deno-health", (_request, response) => {
  response.json({ process: "deno", status: "ok" });
});

app.get("/", (_request, response) => {
  response.send("Independent Deno Express process\n");
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Deno Express process listening on ${port}`);
});
