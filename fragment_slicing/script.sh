spark-submit --driver-memory=32g \
    --conf spark.driver.maxResultSize=16g \
    input.py example_configurations/smiles_randomiser.json