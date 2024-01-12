package com.davybraun.flinkcommerce;

import com.davybraun.flinkcommerce.dto.Transaction;
import com.davybraun.flinkcommerce.serialization.JSONDeserializationSchema;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class DataStreamJob  {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        String topic = "sales_transactions";

        KafkaSource<Transaction> source = KafkaSource.<Transaction>builder()
            .setBootstrapServers("localhost:9092")
            .setTopics(topic)
            .setGroupId("flink-commerce")
            .setStartingOffsets(OffsetsInitializer.earliest())
            .setValueOnlyDeserializer(new JSONDeserializationSchema())
            .build();

        DataStream<Transaction> stream = env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source");
        stream.print();

        env.execute("Flink Streaming Java API Skeleton");
    }
}
