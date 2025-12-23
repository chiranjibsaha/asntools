Windows Setup
=============

Follow these steps on a fresh Windows 10/11 machine to get the project running.

Prerequisites
-------------
- Install `Git for Windows <https://git-scm.com/download/win>`_ and enable "Git from the command line".
- Install `Python 3.11 for Windows <https://www.python.org/downloads/windows/>`_ and check "Add python.exe to PATH".
- (Optional) Install `Visual Studio Build Tools <https://visualstudio.microsoft.com/visual-cpp-build-tools/>`_ if you lack a C++ build chain; most wheels should be prebuilt, but this helps pip when a wheel is missing.

Clone and Configure
-------------------
- Open Windows Terminal or PowerShell.
- Choose a workspace folder, then run::

    git clone <repo-url> asntools
    cd asntools

- Create a virtual environment (PowerShell) and activate it::

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install Dependencies
--------------------
- Upgrade pip and install project + dev extras::

    python -m pip install --upgrade pip
    python -m pip install -e .[dev]

Validate the Setup
------------------
- Run the test suite to confirm the environment works::

    pytest

Common Tips
-----------
- If PowerShell blocks script execution, run ``Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`` once.
- If cloning over SSH, ensure an SSH key is added to ``~/.ssh/id_rsa`` and registered with your Git hosting service.
- To start fresh, deactivate the venv with ``deactivate`` and reactivate later with ``.\\.venv\\Scripts\\Activate.ps1``.
