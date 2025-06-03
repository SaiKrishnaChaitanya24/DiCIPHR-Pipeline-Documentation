
Combinations of Command Line Arguments required to run DTI Pipeline
===================================================================

Reverse PE Scan Available
-------------------------
-s, -i, -d, -t, -p, -T, -o, -z, -e (needs to be 1), -B (needs to be 3 for running the whole DTI Pipeline)
(-z can be 0,1,2, suggested to use 2.)

Example Command to Run When Reverse PE Scan is Available (when slurm is available)
----------------------------------------------------------------------------------

Note - Create output path before running the following command using mkdir –p {Output_Path}

.. code-block:: bash

   sbatch --cpus-per-task=4 --job-name=Combined_ --time=2-00:00:00 --mem=256G --wrap="apptainer run --no-home --bind {Data_Path_Where_Files_are_Available}:/Input --bind {Output_Path}:/output ./Combined-Pipeline/combined_pipeline.sif -s {Subject_Name} -i /input/{T1_File_Name} -d /input/{DWI_File_Name} -o /output -z {mode} -p {PE_DIR} -t /input/{ReversePE_File_Path} -T {Readout_Time} -e {mode} -B 3"
   {mode} - needs to be replaced with corresponding value.
   {PE_DIR} - can be either AP, LR, IS
   {Readout_Time} - can be 0.064 or any similar value

Note – When slurm is not available run the command in quotes (“”) without sbatch.

Reverse PE Scan Not Available
-----------------------------
-s, -i, -d, -o, -z, -e (can either be 0 or 2), -B (needs to be 3 for running the whole DTI Pipeline)
(-e suggested to use is 2) (-z can be 0,1,2, suggested to use 2.)

Note - Create output path before running the following command using mkdir –p {Output_Path}

.. code-block:: bash

   sbatch --cpus-per-task=4 --job-name=Combined_ --time=2-00:00:00 --mem=256G --wrap="apptainer run --no-home --bind {Data_Path_Where_Files_are_Available}:/Input --bind {Output_Path}:/output ./Combined-Pipeline/combined_pipeline.sif -s {Subject_Name} -i /input/{T1_File_Name} -d /input/{DWI_File_Name} -o /output -z {mode} -e {mode} -B 3"
   {mode} - needs to be replaced with corresponding value.

Note – When slurm is not available run the command in quotes (“”) without sbatch.


Index
==================

* :doc:`index`
* :doc:`Installation`
* :doc:`UsageNotes`
* :doc:`batch_array`
* :doc:`PerformanceBenchmarks`
* :doc:`Citations`
* :ref:`search`
