Batch Array Processing Script
=============================

This script is used for batch array processing of multiple subjects utilizing a pipeline executed via SLURM and `apptainer`.

Save the following content into a bash script file (e.g., ``run_batch_pipeline.sh``):

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
    SUBJECT_LIST="{path to a file with subject names, one per line}"
    OUTPUT_PATH="{output path where you want to store your processed files}"

    mkdir -p $OUTPUT_PATH

    # Get subject name based on array task ID
    SUBJECT=$(sed -n "$((SLURM_ARRAY_TASK_ID))p" $SUBJECT_LIST)

    # Define input paths
    SUBJECT_DIR="${BASE_DIR}/${SUBJECT}"
    DWI_IMAGE=$(find "$SUBJECT_DIR" -type f -iname "*DWI*.nii.gz" | head -n 1)
    echo "Found DWI image: $DWI_IMAGE"

    T1_IMAGE=$(find "$SUBJECT_DIR" -type f -iname "*T1*.nii.gz" | head -n 1)
    echo "Found T1 image: $T1_IMAGE"

    # Run the pipeline
    apptainer run --no-home \
        --bind ${BASE_DIR}/${SUBJECT}:${BASE_DIR}/${SUBJECT} \
        --bind $OUTPUT_PATH:/output \
        $SIF_PATH \
        -s $SUBJECT \
        -d $DWI_IMAGE \
        -i $T1_IMAGE \
        -o /output \
        -B 3 -e 1 -F True -z 2

Usage
-----

After saving the script, submit it to the SLURM scheduler using:

.. code-block:: bash

    sbatch run_batch_pipeline.sh

Replace all placeholders (e.g., ``{total number of subjects}``, ``{Base Directory Path}``) with actual values appropriate to your setup.

Index
==================

* :doc:`index`
* :doc:`Installation`
* :doc:`UsageNotes`
* :doc:`RunningDTI`
* :doc:`PerformanceBenchmarks`
* :doc:`Citations`
* :ref:`search`
