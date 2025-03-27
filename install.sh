conda deactivate
conda env create -f env.yml
conda activate diffdec
pip install awswrangler requests-auth-aws-sigv4 torch==2.4.0 numpy imageio
