package com.davybraun.flinkcommerce.dto;

import com.davybraun.flinkcommerce.enums.Currency;
import com.davybraun.flinkcommerce.enums.PaymentMethod;
import com.davybraun.flinkcommerce.enums.ProductBrand;
import java.sql.Timestamp;
import lombok.Data;

@Data
public class Transaction {
    private String transactionId;
    private String productName;
    private String productId;
    private String productCategory;
    private double productPrice;
    private int productQuantity;
    private ProductBrand productBrand;
    private double totalAmount;
    private Currency currency;
    private String customerId;
    private Timestamp transactionDate;
    private PaymentMethod paymentMethod;
}
