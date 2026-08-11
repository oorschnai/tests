import "npm:reflect-metadata@0.2.2";
import "npm:@nestjs/platform-express@11.1.9";
import { NestFactory } from "npm:@nestjs/core@11.1.9";
import { AppModule } from "./src/app.module.ts";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const port = Number(Deno.env.get("PORT") ?? "3000");
  await app.listen(port, "0.0.0.0");
  console.log("Nest server is running on port " + port);
}

await bootstrap();
