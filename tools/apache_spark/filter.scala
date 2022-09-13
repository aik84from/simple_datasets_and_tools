
val file = "raw.data"
val reportDir = "report"
val filter = "example@example.com"

spark.read.textFile(file).filter(line => line.contains(filter)).rdd.saveAsTextFile(reportDir)
