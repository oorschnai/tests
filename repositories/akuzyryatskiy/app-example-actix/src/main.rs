use actix_web::{get, App, HttpResponse, HttpServer, Responder};

#[get("/")]
async fn root() -> impl Responder {
    HttpResponse::Ok()
        .content_type("text/plain; charset=utf-8")
        .body("Timeweb Cloud + Actix = ❤️")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let port = std::env::var("PORT")
        .ok()
        .and_then(|v| v.parse::<u16>().ok())
        .unwrap_or(3000);

    println!("Actix server running on 0.0.0.0:{port}");

    HttpServer::new(|| App::new().service(root))
        .bind(("0.0.0.0", port))?
        .run()
        .await
}
