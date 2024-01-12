#!/bin/bash

# Start Flink cluster (run in jobmanager container)
sleep 30
cd /opt/flink/usrlib/
flink run -c com.davybraun.flinkcommerce.DataStreamJob FlinkCommerce.jar
