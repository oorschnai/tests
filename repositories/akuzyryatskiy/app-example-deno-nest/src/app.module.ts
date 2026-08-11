import { Module } from "npm:@nestjs/common@11.1.9";
import { AppController } from "./app.controller.ts";

@Module({
  controllers: [AppController],
})
export class AppModule {}
