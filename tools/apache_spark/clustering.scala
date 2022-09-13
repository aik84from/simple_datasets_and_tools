import org.apache.spark.ml.clustering.KMeans

val file = "raw.data"
val nClusters = 4

val dataset = spark.read.format("libsvm").load(file)
val model = new KMeans().setK(nClusters).fit(dataset)

model.clusterCenters.foreach(println)
