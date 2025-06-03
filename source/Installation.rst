Installation
===========

Follow these steps if you want to run the pipeline :

**Step 1: Clone the Repository**

Clone the repository to your local machine:

.. code-block:: bash

    git clone https://github.com/SaiKrishnaChaitanya24/DiCIPHR-Pipeline.git

**Step 2: Build the Singularity Container**

Build the `combined_pipeline.sif` container using the provided definition file:

.. code-block:: bash

    sbatch --cpus-per-task=4 --mem=32G --wrap="apptainer build --notest combined_pipeline.sif ./DiCIPHR-Pipeline/Singularity.def"

**Step 3: Test the Singularity Container**

Test the container to ensure it was built correctly. 

.. code-block:: bash

    sbatch --cpus-per-task=2 --mem=32G --wrap="apptainer test combined_pipeline.sif"

If the test is successful, you should see the following message in the .out file:

Container Test Successful, Please Run the Container

Maintainer: Drew Parker <william.parker@pennmedicine.upenn.edu> and Sai Krishna Chaitanya Annavazala <SaiKrishna.Annavazala@pennmedicine.upenn.edu>

Version: 1.0.0


**Step 4: Create Output Directory**

Create a directory to store output files:

.. code-block:: bash

    mkdir -p {output_path}

Index
==================

* :doc:`index`
* :doc:`UsageNotes`
* :doc:`RunningDTI`
* :doc:`PerformanceBenchmarks`
* :doc:`Citations`
* :ref:`search`
