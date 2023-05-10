## Development
1. Setup a virtual env: `python -m venv .venv && source .venv/bin/activate`
2. Install the package: `pip install -e . && pyenv rehash`
3. Run: `solara run bulk_labeling/main.py`

Any changes you make to the app should reflect in realtime

### Note: `SentenceTransformers` doesn't play nicely with solara
If you are going to be developing, I strongly recommend commenting out
the few lines in [ml.py](bulk_labeling/utils/ml.py):
https://github.com/Ben-Epstein/bulk-labeling-solara/blob/e529dd44061d2647a49b3d53f53b22c59149fde3/bulk_labeling/utils/ml.py#L5
https://github.com/Ben-Epstein/bulk-labeling-solara/blob/e529dd44061d2647a49b3d53f53b22c59149fde3/bulk_labeling/utils/ml.py#L9
https://github.com/Ben-Epstein/bulk-labeling-solara/blob/e529dd44061d2647a49b3d53f53b22c59149fde3/bulk_labeling/utils/ml.py#L13

**And uncomment**
https://github.com/Ben-Epstein/bulk-labeling-solara/blob/e529dd44061d2647a49b3d53f53b22c59149fde3/bulk_labeling/utils/ml.py#L15

For some reason, on a page reload, solara breaks if these lines are running.  
It will also make prototyping faster because you won't be actually encoding strings.
