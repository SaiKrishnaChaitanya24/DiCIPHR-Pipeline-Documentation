Usage Notes
===========

Command-Line Arguments
----------------------

.. list-table::
   :header-rows: 1

   * - Argument
     - Description
   * - ``-s``
     - Input subject name
   * - ``-i``
     - Raw T1 Image
   * - ``-d``
     - DWI Image
   * - ``-o``
     - Output Directory
   * - ``-t``
     - Topup file
   * - ``-p``
     - Phase encoding value
   * - ``-T``
     - Readout Time
   * - ``-w``
     - Work directory (set to current path)
   * - ``-m``
     - Input mask
   * - ``-e``
     - Modes available:

       **1**: Only DTI Preprocess

       **2**: Till registration DTI to T1

       **Default**: The whole pipeline


Expected Arguments
------------------

For ``notopup``:
   - ``-s``
   - ``-i``
   - ``-d``
   - ``-o``

For ``topup``:
   - ``-s``
   - ``-i``
   - ``-d``
   - ``-o``
   - ``-t``
   - ``-T``
   - ``-p``


Index
==================

* :doc:`index`
* :doc:`Installation`
* :doc:`RunningDTI`
* :ref:`search`
