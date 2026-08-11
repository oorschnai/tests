import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getRoot(): string {
    return 'Timeweb Cloud + Nest on Bun = ❤️';
  }
}
