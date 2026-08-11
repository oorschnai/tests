'use strict';
const Hapi = require('@hapi/hapi');
const port = Number(process.env.PORT || 3000);
const init = async () => {
  const server = Hapi.server({
    port,
    host: '0.0.0.0',
  });
  server.route({
    method: 'GET',
    path: '/',
    handler: () => 'Timeweb Cloud + Hapi on Bun = тЭдя╕П',
  });
  await server.start();
  console.log('Hapi server is running on %s', server.info.uri);
};
process.on('unhandledRejection', (err) => {
  console.error(err);
  process.exit(1);
});
init();
