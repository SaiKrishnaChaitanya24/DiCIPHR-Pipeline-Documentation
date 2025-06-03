Batch Array Processing Script
=============================

This script is used for batch array processing of multiple subjects utilizing the pipeline.

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=run_pipeline
    #SBATCH --output=logs/%A_%a.out
    #SBATCH --error=logs/%A_%a.err
    #SBATCH --array=1-{total number of subjects}
    #SBATCH --time=1-00:00:00
    #SBATCH --mem=196G
    #SBATCH --cpus-per-task=4
    #SBATCH --partition={partition_name}

    # Base paths
    BASE_DIR="{Base Directory Path}"
    SIF_PATH="{sif image path}"
    SUBJECT_LIST="{arrage your subject names in a single column format}"
    OUTPUT_PATH="{output path where you want to store your processed files}"

    mkdir -p $OUTPUT_PATH

    # Get subject name
    SUBJECT=$(sed -n "$((SLURM_ARRAY_TASK_ID))p" $SUBJECT_LIST)

    # Define input paths
    SUBJECT_DIR="${BASE_DIR}/${SUBJECT}"
    DWI_IMAGE=$(find "$SUBJECT_DIR" -type f -iname "*DWI*.nii.gz" | head -n 1)
    echo $DWI_IMAGE
    T1_IMAGE=$(find "$SUBJECT_DIR" -type f -iname "*T1*.nii.gz" | head -n 1)
    echo $T1_IMAGE

    apptainer run --no-home --bind ${BASE_DIR}/${SUBJECT}:${BASE_DIR}/${SUBJECT} --bind $OUTPUT_PATH:/output $SIF_PATH -s $SUBJECT -d $DWI_IMAGE -i $T1_IMAGE -o /output -B 3 -e 1 -F True -z
