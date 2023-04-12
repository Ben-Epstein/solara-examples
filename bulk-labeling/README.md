# bulk-labeling-solara
A tool for bulk labeling, built in Solara!

I'm trying to rebuild my original [bulk-labeling](https://github.com/rungalileo/bulk-labeling/) app, which was Streamlit, in [Solara](https://github.com/widgetti/solara) so it can be a bit more scalable, customizable, and robust to new features!

I also want to learn how to use solara :) 


## Roadmap
- [ ] Allow the user to download the labeled file :D (https://github.com/widgetti/solara/pull/30)
- [ ] Fix the layout of embeddings and dataframe so they are next to each other (not stacked)<br>Also the solara message on the bottom right is in a bad spot <img width="750" height="400" alt="image" src="https://user-images.githubusercontent.com/22605641/216855251-c8f71922-3358-4383-9e2b-b8c73bfb4c41.png">

- [ ] Get a more fun animation for when the embeddings are being calculated. Would also be cool if we could update them with the logs from UMAP or tqdm
- [ ] Fix mypy issues <img width="1254" alt="image" src="https://user-images.githubusercontent.com/22605641/216855155-0477352c-9707-4588-849b-9d630dc72339.png">
- [ ] The "reset filters" button should really be a switch, not a checkbox. It doesn't look great<br> <img width="288" alt="image" src="https://user-images.githubusercontent.com/22605641/216855320-bad0c6f3-07bf-4202-baba-512396e8b703.png">
- [ ] Add a nice readme like what I have in the [streamlit version](https://github.com/rungalileo/bulk-labeling) - We should wait until the visual issues are fixed so we don't need to redo it 
- [ ] Write the blog on how I built it (same as above, wait until it's in a better state)
- [ ] Deploy on solara cloud?!? 🚀

 


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
