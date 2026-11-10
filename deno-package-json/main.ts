import express from "express";

const app = express();
const port = Number(Deno.env.get("PORT") ?? "8000");

app.get("/", (_request, response) => {
  response.json({
    status: "ok",
    case: "deno-package-json",
    express: "4.21.2",
  });
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Frameworkless Deno package.json test is listening on ${port}`);
});
