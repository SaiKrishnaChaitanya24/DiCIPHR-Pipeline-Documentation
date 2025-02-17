Running DiCIPHR-Pipeline
========================

Running the Pipeline
--------------------

Follow these steps to run the DiCIPHR-Pipeline. Ensure you have the necessary permissions and resources.

**Step 1: Clone the Repository**

Clone the repository to your local machine:

.. code-block:: bash

    git clone https://github.com/SaiKrishnaChaitanya24/DiCIPHR-Pipeline.git

**Step 2: Build the Singularity Container**

Build the `diciphr_pipeline.sif` container using the provided definition file:

.. code-block:: bash

    cd DiCIPHR-Pipeline
    sbatch --cpus-per-task=4 --mem=32G --wrap="singularity build --notest diciphr_pipeline.sif Singularity.def"

**Step 3: Test the Singularity Container**

Test the container to ensure it was built correctly. 

.. code-block:: bash

    sbatch --cpus-per-task=2 --mem=32G --wrap="apptainer test diciphr_pipeline.sif"

If the test is successful, you should see the following message in the .out file:

Container Test Successful, Please Run the Container

Maintainer: Drew Parker <william.parker@pennmedicine.upenn.edu> and Sai Krishna Chaitanya Annavazala <SaiKrishna.Annavazala@pennmedicine.upenn.edu>

Version: 1.0.0


**Step 4: Create Output Directory**

Create a directory to store output files:

.. code-block:: bash

    mkdir -p {output_path}

**Step 5: Run the Pipeline**

Run the pipeline using the Singularity container, specifying the subject name, T1 image, DWI image, and output directory. Use absolute paths for T1 and DWI `.nii` files. Choose between the following commands based on your requirements:

**For Notopup:**

.. code-block:: bash

    if you are already in the DiCIPHR-Pipeline directory run below command, else change your current path to where DiCIPHR-Pipeline directory is and run the below command
    sbatch --cpus-per-task=4 --job-name=dti --mem=32G --wrap="singularity run --no-home --bind /folder_path:/folder_path --bind {output_path}:/output diciphr_pipeline.sif -s {subject_name} -i {image_path} -d {DWI_absolute_path} -o /output"

**For Topup:**

.. code-block:: bash

    if you are already in the DiCIPHR-Pipeline directory run below command, else change your current path to where DiCIPHR-Pipeline directory is and run the below command
    sbatch --cpus-per-task=4 --job-name=dti --mem=32G --wrap="singularity run --no-home --bind /folder_path:/folder_path --bind {output_path}:/output diciphr_pipeline.sif -s {subject_name} -i {image_path} -d {DWI_absolute_path} -o /output -t {topup file} -P {Phase Encoding} -T {Readout Time}"

**Notes:**
- When using files that require topup, specify the phase encoding with `-P` and the readout time with `-T`.
- Replace `/folder_path:/folder_path` with the absolute path where your data is stored.
- Replace `{subject_name}`, `{image_path}`, and `{DWI_absolute_path}` with actual values.

--------------------

Recommended SLURM Options
------------------------

Add the `--propagate=NONE` option for recommended SLURM settings when using the `sbatch` command.

--------------------

Pipeline Modes
--------------

Run the pipeline in three modes:

1. **Only DTI_Preprocess**: Specify `-e 1` in the `sbatch` command.
2. **Till Registration Process**: Specify `-e 2` in the `sbatch` command.
3. **Full Pipeline**: No `-e` option required.

Index
==================

* :doc:`index`
* :doc:`UsageNotes`
* :ref:`search`
