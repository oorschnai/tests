import { Controller, Get } from "npm:@nestjs/common@11.1.9";

@Controller()
export class AppController {
  @Get()
  getRoot(): string {
    return "Timeweb Cloud + Nest on Deno";
  }
}
