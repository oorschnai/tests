import express from "npm:express@4.21.2";

const app = express();
const port = Number(Deno.env.get("PORT") ?? "3000");

app.get("/", (_req, res) => {
  res.send("Timeweb Cloud + Express on Deno");
});

app.listen(port, "0.0.0.0", () => {
  console.log("Express server is running on port " + port);
});
