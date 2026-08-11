'use strict';

const puppeteer = require('puppeteer');

async function helloWorld() {
  const browser = await puppeteer.launch({
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || '/usr/bin/google-chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();

  await page.goto('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program');

  const firstPar = await page.$eval('#mw-content-text p', el => el.innerText);

  console.log(firstPar); // A "Hello, World!" program is a computer program that outputs ...

  await browser.close();
}

helloWorld();
