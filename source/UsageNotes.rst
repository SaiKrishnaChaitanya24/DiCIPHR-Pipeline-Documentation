
Usage Notes
===========

Command-Line Arguments
----------------------

.. list-table::
   :header-rows: 1

   * - Argument
     - Description
   * - `-s`
     - Subject Name
   * - `-i`
     - T1 Image
   * - `-d`
     - DWI Image
   * - `-t`
     - Topup Image (if available)
   * - `-p`
     - Phase Encoding Direction (e.g., AP, LR, IS)
   * - `-T`
     - Readout Time (e.g., 0.064)
   * - `-o`
     - Output Directory Path
   * - `-z`
     - Denoising Mode:
       
       **0**: No denoising  

       **1**: MP-PCA only  

       **2**: Gibbs de-ringing + MP-PCA (recommended)
   * - `-e`
     - Distortion Correction Mode:
       
       **0**: No correction (for non-human or tumor cases)  

       **1**: Use Topup (requires reverse PE scan)  

       **2**: Use Synb0-Disco (requires T1 and DWI)
   * - `-B`
     - Pipeline Mode:
       
       **1**: Synb0-Disco, DTI Preprocess, Fernet  

       **2**: + BrainMaGe, DTI to T1 Registration  

       **3**: + T1 to Eve Registration, ROI Stats (Full DTI Pipeline)  

       **4**: + Freesurfer, Structural Connectivity Pipeline
   * - `-F`
     - Set to `True` to run Freesurfer (required for Structural Connectivity)

Expected Argument Combinations
------------------------------

**If Reverse PE Scan is Available (`-e 1`)**:
   - `-s`, `-i`, `-d`, `-t`, `-p`, `-T`, `-o`, `-z`, `-e`, `-B`

**If Reverse PE Scan is Not Available (`-e 0` or `2`)**:
   - `-s`, `-i`, `-d`, `-o`, `-z`, `-e`, `-B`

**Recommended Settings**:
   - `-z`: 2 (for best denoising)
   - `-e`: 2 (if no reverse PE scan)


Index
==================

* :doc:`index`
* :doc:`Installation`
* :doc:`RunningDTI`
* :doc:`batch_array`
* :doc:`PerformanceBenchmarks`
* :doc:`Citations`
* :ref:`search`
