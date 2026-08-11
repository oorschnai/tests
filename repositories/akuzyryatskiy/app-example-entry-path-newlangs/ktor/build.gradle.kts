val kotlin_version: String by project
val logback_version: String by project

plugins {
    kotlin("jvm") version "2.3.20"
    id("io.ktor.plugin") version "3.4.3"
}

group = "com.timeweb"
version = "1.0.0"

application {
    mainClass.set("com.timeweb.ApplicationKt")
}

kotlin {
    jvmToolchain(17)
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor:ktor-server-core-jvm")
    implementation("io.ktor:ktor-server-netty-jvm")
    implementation("ch.qos.logback:logback-classic:$logback_version")
    testImplementation("io.ktor:ktor-server-test-host-jvm")
    testImplementation("org.jetbrains.kotlin:kotlin-test-junit:$kotlin_version")
}
