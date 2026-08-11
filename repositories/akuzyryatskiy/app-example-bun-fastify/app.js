'use strict';
const fastify = require('fastify')({ logger: true });
const port = Number(process.env.PORT || 3000);
fastify.get('/', async () => {
  return { message: 'Timeweb Cloud + Fastify on Bun = тЭдя╕П' };
});
const start = async () => {
  try {
    await fastify.listen({ port, host: '0.0.0.0' });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};
start();
