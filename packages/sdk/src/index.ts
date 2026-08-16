export interface ClientOptions {
  baseUrl: string;
  apiKey: string;
}

export interface Check {
  code: string;
  name: string;
  status: "up" | "down" | "grace" | "paused";
}

export class PlatformClient {
  constructor(private readonly options: ClientOptions) {}

  private async request<T>(path: string): Promise<T> {
    const response = await fetch(`${this.options.baseUrl}${path}`, {
      headers: { "X-Api-Key": this.options.apiKey },
    });
    if (!response.ok) {
      throw new Error(`${path} failed with ${response.status}`);
    }
    return (await response.json()) as T;
  }

  listChecks(): Promise<{ items: Check[] }> {
    return this.request("/api/v3/checks");
  }

  ping(code: string): Promise<unknown> {
    return this.request(`/ping/${code}`);
  }
}
