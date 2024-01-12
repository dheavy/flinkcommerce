package com.davybraun.flinkcommerce.enums;

import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.annotation.JsonProperty;

public enum PaymentMethod {
    @JsonProperty("credit_card")
    CREDIT_CARD,
    @JsonProperty("debit_card")
    DEBIT_CARD,
    @JsonProperty("paypal")
    PAYPAL,
}
