use axum::{routing::get, Router};
use tokio::net::TcpListener;

#[tokio::main]
async fn main() {
    let port = std::env::var("PORT")
        .ok()
        .and_then(|v| v.parse::<u16>().ok())
        .unwrap_or(3000);

    let app = Router::new().route("/", get(root));
    let listener = TcpListener::bind(("0.0.0.0", port)).await.unwrap();

    println!("Axum server running on 0.0.0.0:{port}");
    axum::serve(listener, app).await.unwrap();
}

async fn root() -> &'static str {
    "Timeweb Cloud + Axum = ❤️"
}
