package com.davybraun.flinkcommerce.enums;

import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.annotation.JsonProperty;

public enum ProductBrand {
    @JsonProperty("apple")
    APPLE,
    @JsonProperty("samsung")
    SAMSUNG,
    @JsonProperty("xiaomi")
    XIAOMI,
    @JsonProperty("huawei")
    HUAWEI,
    @JsonProperty("sony")
    SONY,
}
