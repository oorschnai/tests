import express from "express";

const app = express();
const port = Number.parseInt(process.env.NODE_PORT ?? "3000", 10);

app.get("/node-health", (_request, response) => {
  response.json({ process: "node", status: "ok" });
});

app.get("/", (_request, response) => {
  response.send("Independent Node.js Express process\n");
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Node.js Express process listening on ${port}`);
});
