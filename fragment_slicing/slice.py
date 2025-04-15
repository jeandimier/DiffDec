import argparse
import json
import subprocess
from pathlib import Path

fragment_slicing_dir = Path(__file__).parent.resolve()
output_dir = fragment_slicing_dir / "output_dir"

# Check we are in the good directory
assert (fragment_slicing_dir / "input.py").is_file(), (
    f"The input.py file was not located in the folder of the launched file {str(Path(__file__))}. Perhaps one those files was moved?"
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--smiles",
        type=str,
        help="The path of the file containing all the smiles of molecules to slice",
    )
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(e.message)

    # Check the input files
    if Path(args.smiles).is_file():
        input_dataset_path = args.smiles
    else:
        raise FileNotFoundError(f"Impossible to find the SMILES file: {args.smiles}")

    reactions_file_path = fragment_slicing_dir / "data" / "reaction.smirks"
    filter_conditions_JSON_path = output_dir / "filter_conditions.json"

    cfg = {
        "run_type": "reaction_based_slicing",
        "parameters": {
            "input_file": input_dataset_path,
            "output_path": output_dir / "sliced",
            "output_smiles_file": output_dir / "reaction_smiles",
            "conditions_file": filter_conditions_JSON_path,
            "reactions_file": reactions_file_path,
            "max_cuts": 1,  # the maximum number of cuts to perform on each molecule.
            "number_of_partitions": 1000,  # relevant for PySpark. Do not change.
            "validate_randomization": True,  # check that randomised molecules correspond to the originals.
        },
    }
    for key, value in cfg["parameters"].items():
        try:
            str_value = value.as_posix()
            cfg["parameters"][key] = str_value
        except Exception:
            pass

    # write the config file to the disc
    cfg_JSON_path = output_dir / "reaction_slicing_config.json"
    with open(cfg_JSON_path.as_posix(), "w") as f:
        json.dump(cfg, f, indent=4, sort_keys=False)

    # Define the paths
    outfile_stderr = output_dir / "run.err"

    # Execute the spark-submit command
    # args = shlex.split(command_line)
    with open(outfile_stderr, "w") as stderr_file:
        subprocess.run(
            [
                "conda",
                "run",
                "-n",
                "diffdec",
                "--no-capture-output",
                "spark-submit",
                "--driver-memory=80g",
                "--conf",
                "spark.driver.maxResultSize=32g",
                "input.py",
                str(cfg_JSON_path),
            ],
            stdout=subprocess.PIPE,
            stderr=stderr_file,
            check=False,
            cwd=fragment_slicing_dir,
        )
