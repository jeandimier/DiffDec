conda deactivate
conda env create -f env.yml
conda activate diffdec
pip install awswrangler requests-auth-aws-sigv4 mlflow
