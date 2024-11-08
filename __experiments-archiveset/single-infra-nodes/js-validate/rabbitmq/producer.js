const amqp = require('amqplib/callback_api');
const dotenv = require('dotenv');
const path = require('path');

dotenv.config({
    path: path.join(__dirname, '..', '..', '.env'),
})

const {
    RABBITMQ_DEFAULT_USER,
    RABBITMQ_DEFAULT_PASS,
} = process.env;

const RABBITMQ_HOST = `amqp://${RABBITMQ_DEFAULT_USER}:${RABBITMQ_DEFAULT_PASS}@localhost:5672`;
const QUEUE_NAME = 'test_queue';

amqp.connect(RABBITMQ_HOST, (err, conn) => {
  if (err) {
    throw err;
  }
  conn.createChannel((err, channel) => {
    if (err) {
      throw err;
    }
    channel.assertQueue(QUEUE_NAME, {
      durable: false
    });
    const msg = 'Hello, RabbitMQ!';
    channel.sendToQueue(QUEUE_NAME, Buffer.from(msg));
    console.log(` [x] Sent ${msg}`);
    setTimeout(() => {
      conn.close();
      process.exit(0);
    }, 500);
  });
});