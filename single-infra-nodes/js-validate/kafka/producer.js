const { Kafka, Partitioners } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-producer',
  brokers: ['localhost:9092'],  // Kafka 브로커의 호스트 및 포트
  /*  
{"level":"WARN","timestamp":"2024-07-16T18:52:25.937Z","logger":"kafkajs","message":"KafkaJS v2.0.0 switched default partitioner. To retain the same partitioning behavior as in previous versions, create the producer with the option \"createPartitioner: Partitioners.LegacyPartitioner\". See the migration guide at https://kafka.js.org/docs/migration-guide-v2.0.0#producer-new-default-partitioner for details. Silence this warning by setting the environment variable \"KAFKAJS_NO_PARTITIONER_WARNING=1\""}
  */
  createPartitioner: Partitioners.LegacyPartitioner // 기존 파티셔너 사용 설정
});

const producer = kafka.producer();

const runProducer = async () => {
  await producer.connect();

  // 메시지 전송 예시
  await producer.send({
    topic: 'test-topic',
    messages: [
      { value: 'Hello Kafka!' },
    ],
  });

  console.log('Message sent successfully!');
  await producer.disconnect();
};

runProducer().catch(console.error);