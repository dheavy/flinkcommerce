package com.davybraun.flinkcommerce.serialization;

import com.davybraun.flinkcommerce.dto.Transaction;
import java.io.IOException;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.ObjectMapper;

public class JSONDeserializationSchema implements DeserializationSchema<Transaction> {

    private final ObjectMapper ObjectMapper = new ObjectMapper();

    @Override
    public TypeInformation<Transaction> getProducedType() {
        return TypeInformation.of(Transaction.class);
    }

    @Override
    public Transaction deserialize(byte[] message) throws IOException {
        return ObjectMapper.readValue(message, Transaction.class);
    }

    @Override
    public boolean isEndOfStream(Transaction nextElement) {
        return false;
    }

}
