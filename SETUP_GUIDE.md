# Setup Guide — Geomorphological Hazards of Slopes

*A step-by-step guide for getting Python, Git, and the course notebooks running on your laptop.*

**You will install:** Python (3.11 or newer), Git, Visual Studio Code, and a handful of Python packages inside an isolated environment. On a decent internet connection this takes about 20–30 minutes.

**Before you start:** make sure you have administrator rights on the laptop you plan to use, otherwise some installers will refuse. You do **not** need a GitHub account just to read the course materials — `git clone` works against the public repository without one.

> Throughout this guide, lines that begin with `$` are commands to type at a terminal prompt. The `$` itself is not part of the command. On Windows, "terminal" means PowerShell or Git Bash; on macOS and Linux, it means Terminal.

---

## 1. Install Python

We use **Python 3.11 or newer**. The notebooks were developed and tested with 3.12.

### Windows

1. Go to <https://www.python.org/downloads/> and download the latest stable installer.
2. Run the installer. **Critical: tick the box "Add python.exe to PATH"** at the bottom of the first installer page before clicking *Install Now*.
3. Open PowerShell and verify:
   ```
   $ python --version
   ```
   You should see something like `Python 3.12.x`.

### macOS

Easiest route is Homebrew (<https://brew.sh>):
```
$ brew install python@3.12
```
Or download the `.pkg` installer from <https://www.python.org/downloads/macos/>.

Verify:
```
$ python3 --version
```

### Linux (Ubuntu/Debian)

```
$ sudo apt update
$ sudo apt install python3 python3-venv python3-pip
$ python3 --version
```

---

## 2. Install Git

Git is the version-control tool we use to share the notebooks.

- **Windows:** download from <https://git-scm.com/download/win> and install with the default options. This also gives you *Git Bash*, a useful Unix-style terminal.
- **macOS:** ships with the Xcode Command Line Tools. Run `xcode-select --install` once. Or `brew install git`.
- **Linux:** `sudo apt install git`.

Verify on any OS:
```
$ git --version
```

---

## 3. Install Visual Studio Code

VS Code is a free, lightweight editor with excellent Python and Jupyter support.

1. Download and install from <https://code.visualstudio.com/>.
2. Open VS Code, then open the Extensions pane (`Ctrl+Shift+X` on Windows/Linux, `Cmd+Shift+X` on macOS) and install these two extensions:
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)

That is the minimum. Pylance (the language server) installs automatically with the Python extension.

> If you already prefer JupyterLab or PyCharm, that is fine — the rest of this guide still applies. JupyterLab installs automatically with the requirements below and runs in the browser via `jupyter lab`.

---

## 4. Clone the course repository

Open a terminal in the folder where you want the course code to live, then:

```
$ git clone https://github.com/<INSTRUCTOR-WILL-SHARE-URL>.git
$ cd <repo-folder-name>
```

Replace the placeholder with the actual URL the instructor sends. After cloning you will have a local copy of all notebooks, figures, and shared code.

**To get updates during the course** — for example, when a new notebook is added between teaching days — run:
```
$ git pull
```
inside the repo folder. This is non-destructive as long as you have not edited the instructor's files. If you want to experiment, copy a notebook to your own filename first (`03_mohr_coulomb.ipynb` → `03_mohr_coulomb_MYNAME.ipynb`).

---

## 5. Create a virtual environment

A *virtual environment* is an isolated copy of Python — packages installed in it never touch your system Python. This is the single most important habit for keeping projects from interfering with each other.

From **inside the repo folder**:

### Windows (PowerShell)

```
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
```

If PowerShell refuses the activation script with an *execution policy* error, run this once, then try again:
```
$ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### macOS / Linux

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

When the env is active, your prompt is prefixed with `(.venv)`. To leave the env later, just type `deactivate`.

---

## 6. Install the required packages

With the venv still active:

```
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

This installs `numpy`, `matplotlib`, `jupyterlab`, `ipykernel`, `ipywidgets`, `pandas`, and `scipy`. Later in the course we will add geospatial libraries (`rasterio`, `geopandas`) for the LiDAR notebook — that addition will come in an updated `requirements.txt`, so re-run the same `pip install -r requirements.txt` after a `git pull`.

---

## 7. Register the env as a Jupyter kernel

This step makes the venv discoverable to Jupyter and to VS Code's notebook kernel picker:

```
$ python -m ipykernel install --user --name silesia-slopes --display-name "Python (silesia-slopes)"
```

You only need to do this once per machine.

---

## 8. Open a notebook and verify

Open VS Code in the repo folder:
```
$ code .
```

In VS Code's file explorer, open `notebooks/03_mohr_coulomb.ipynb`. Click the kernel picker in the top-right of the notebook and choose **Python (silesia-slopes)**. Then click ▶ on the first code cell — or press `Shift+Enter` to run it and move to the next.

If the imports run without error and the Mohr circle plot appears, your setup is complete.

To run JupyterLab in the browser instead:
```
$ jupyter lab
```

---

## Troubleshooting

- **`pip: command not found`** — your venv is not active. Re-run the activation step from §5.
- **VS Code does not list your env in the kernel picker** — open the Command Palette (`Ctrl/Cmd+Shift+P`), run *Python: Select Interpreter*, and pick the entry inside `.venv`. Then reload the notebook.
- **`ModuleNotFoundError: No module named 'style'`** — open the notebook from inside the `notebooks/` folder. The notebooks import `style.py` from the same directory they live in.
- **Sliders / widgets do not appear** — `pip install --upgrade ipywidgets` inside the venv, then restart the kernel (the circular-arrow icon at the top of the notebook).
- **Plots open in a separate window instead of inline** — add `%matplotlib inline` as the first line of the setup cell.
- **A package install fails on Windows with a compiler error** — make sure you are on Python 3.11 or 3.12. Wheels (pre-built binaries) are available for those versions and avoid the need to compile anything locally.

---

## Alternative: conda / Miniconda

If you already use Miniconda or Anaconda, skip §5–§6 and instead:

```
$ conda create -n silesia-slopes python=3.12
$ conda activate silesia-slopes
$ pip install -r requirements.txt
$ python -m ipykernel install --user --name silesia-slopes --display-name "Python (silesia-slopes)"
```

---

## You are ready

If `03_mohr_coulomb.ipynb` runs end-to-end without error and the interactive Mohr circle responds to its sliders, your setup is complete. Bring the laptop to class with the env already activated and a recent `git pull` done that morning.

If anything in this guide does not work for you, send a screenshot of the error to the instructor before class — most setup issues are easier to fix over email than at the start of a teaching block.
