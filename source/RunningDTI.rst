Running DiCIPHR-Pipeline
================

Running the Pipeline
--------------------

Follow the steps below to run the DiCIPHR-Pipeline. Ensure you have the necessary permissions and resources to execute these commands.

**Step 1: Clone the Repository**

First, clone the repository to your local machine using the following command:

.. code-block:: bash

    git clone https://github.com/SaiKrishnaChaitanya24/DiCIPHR-Pipeline.git

**Step 2: Build the Singularity Container**

Build the `diciphr_pipeline.sif` Singularity container using the provided Singularity definition file. This ensures you have the required environment to run the pipeline. Use the following command:

.. code-block:: bash

    sbatch --cpus-per-task=4 --mem=32G --wrap="singularity build --notest ./DiCIPHR-Pipeline/diciphr_pipeline.sif ./DiCIPHR-Pipeline/Singularity.def"

**Step 3: Test the Singularity Container**

Ensure that the Singularity container was built correctly by testing it with the following command:

.. code-block:: bash

    singularity test ./DiCIPHR-Pipeline/diciphr_pipeline.sif

**Step 4: Create Output Directory**

Create a directory to store the output files generated by the pipeline. Use the command below:

.. code-block:: bash

    mkdir -p {output_path}

**Step 5: Run the Pipeline**

Run the pipeline using the Singularity container. You need to specify the subject name, the absolute path to the T1 image, the absolute path to the DWI image, and the output directory. The T1 and DWI images should be `.nii` files, and the T1 image must be cropped. Use one of the commands below, based on your requirements:

**For Notopup:**

.. code-block:: bash

    sbatch --cpus-per-task=4 --job-name=dti --mem=32G --wrap="singularity run --no-home --bind /folder_path:/folder_path --bind {output_path}:/output ./DiCIPHR-Pipeline/diciphr_pipeline.sif -s {subject_name} -i {image_path} -d {DWI_absolute_path} -o /output"

**For Topup:**

.. code-block:: bash

    sbatch --cpus-per-task=4 --job-name=dti --mem=32G --wrap="singularity run --no-home --bind /folder_path:/folder_path --bind {output_path}:/output ./DiCIPHR-Pipeline/diciphr_pipeline.sif -s {subject_name} -i {image_path} -d {DWI_absolute_path} -o /output -t {topup file} -P {Phase Encoding} -T {Readout Time}"

**Note**: When using the pipeline for files that require topup, specify the phase encoding with `-P` and the readout time with `-T` in the command above.

**Note**: Replace `/folder_path:/folder_path` with the absolute path where your data is stored.

Remember to replace `{subject_name}`, `{image_path}`, and `{DWI_absolute_path}` with the actual values for your specific data (use absolute paths).

--------------------

Recommended SLURM Options
-------------------- 

When using the `sbatch` command to run the container, add the `--propagate=NONE` option for recommended SLURM settings.

--------------------

Pipeline Modes
--------------------

You can run the pipeline in three modes:

1. **Only DTI_Preprocess**: Specify `-e 1` in the `sbatch` command.

2. **Till Registration Process**: Specify `-e 2` in the `sbatch` command.

3. **Full Pipeline**: No `-e` option required.

Indices and tables
==================

* :doc:`index`
* :ref:`search`
