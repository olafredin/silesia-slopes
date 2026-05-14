# Geomorphological Hazards of Slopes

Short-course materials for the *International Environmental Doctoral School* at the **Centre for Polar Studies, University of Silesia in Katowice**. 16 hours over three days, 2 ECTS.

*Lecturer: Ola Fredin (NTNU, Trondheim).*

## What the course is about

This course introduces the fundamentals of slope instability and geohazards in steep terrain — landslides, debris flows, debris falls, rock falls. It links soil-mechanical principles (effective stress, Mohr–Coulomb, infinite-slope stability) to real-world slope processes, with regional examples from the Carpathians, Sudetes, Tatras, Norwegian fjord slopes, and global hotspots.

Teaching combines short lectures with hands-on Jupyter-notebook exercises. The notebooks in this repository run in parallel with the slide decks: theory and key equations on the slides, computation and visualisation in the notebooks.

## Getting started

See [**SETUP_GUIDE.md**](SETUP_GUIDE.md) for step-by-step installation instructions (Python, Git, VS Code, virtual environment, packages). The short version:

```
git clone <this-repo-url>
cd <repo-folder>
python -m venv .venv
source .venv/bin/activate            # macOS / Linux
# .venv\Scripts\Activate.ps1         # Windows PowerShell
pip install -r requirements.txt
python -m ipykernel install --user --name silesia-slopes --display-name "Python (silesia-slopes)"
```

Then open any notebook under `notebooks/` and select the **Python (silesia-slopes)** kernel.

## Repository layout

```
silesia-slopes/
├── README.md            ← you are here
├── SETUP_GUIDE.md       ← installation instructions
├── requirements.txt
├── .gitignore
└── notebooks/
    ├── style.py         ← shared matplotlib style
    ├── 00_template.ipynb
    ├── 03_mohr_coulomb.ipynb
    ├── 04_infinite_slope.ipynb
    └── …
```

The `notebooks/figures/` folder is generated when the notebooks are run; it is not committed to the repository.

## Notebook portfolio

Numbering matches the order in which topics are introduced in the lectures.

| #  | Notebook                       | Topic                                                |
|----|--------------------------------|------------------------------------------------------|
| 00 | `00_template.ipynb`            | Structural template (copy to start a new notebook)   |
| 01 | `01_geohazards_intro.ipynb`    | Hazard vs. risk; Hungr et al. (2014) classification  |
| 02 | `02_effective_stress.ipynb`    | Effective stress and pore-water pressure             |
| 03 | `03_mohr_coulomb.ipynb`        | Mohr circles and the Mohr–Coulomb failure criterion  |
| 04 | `04_infinite_slope.ipynb`      | Infinite-slope FS, saturation, critical depth        |
| 05 | `05_rainfall_triggers.ipynb`   | Rainfall infiltration and intensity–duration thresholds |
| 06 | `06_rockfall_trajectory.ipynb` | Shadow-angle / energy-line methods                   |
| 07 | `07_debris_flow_runout.ipynb`  | α–β regression and Monte-Carlo runout                |
| 08 | `08_lidar_hillshade.ipynb`     | LiDAR/DEM hillshade and susceptibility mapping       |

## Updating during the course

Pull updates between teaching days with:
```
git pull
```
If `requirements.txt` has changed, re-run `pip install -r requirements.txt` inside the activated venv.

## Assessment

Graded on a final written exam (see the course description for details). Active participation in notebook laboratories is mandatory but not graded.

## Licence

Course materials are released under the [Creative Commons Attribution 4.0 International Licence (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/). You are welcome to reuse and adapt the materials with attribution.

## Contact

For setup problems before the course, email the instructor (preferably with a screenshot of the error). For everything else, see you in Katowice.
