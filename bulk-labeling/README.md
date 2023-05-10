# bulk-labeling-solara
A tool for bulk labeling, built in Solara!

I'm trying to rebuild my original [bulk-labeling](https://github.com/rungalileo/bulk-labeling/) app, which was Streamlit, in [Solara](https://github.com/widgetti/solara) so it can be a bit more scalable, customizable, and robust to new features!

I also want to learn how to use solara :)


## Roadmap
- [X] Allow the user to download the labeled file :D (https://github.com/widgetti/solara/pull/30)
- [X] Fix the layout of embeddings and dataframe so they are next to each other (not stacked)<br>Also the solara message on the bottom right is in a bad spot <img width="750" height="400" alt="image" src="https://user-images.githubusercontent.com/22605641/216855251-c8f71922-3358-4383-9e2b-b8c73bfb4c41.png">
- [X] Use `solara.progress` for UMAP
- [X] Remove `.use` from the code
- [X] Camel Case my components
- [X] Move to the new `solara.reactive`
- [ ] Get a more fun animation for when the embeddings are being calculated. Would also be cool if we could update them with the logs from UMAP or tqdm
- [ ] The "reset filters" button should really be a switch, not a checkbox. It doesn't look great<br> <img width="288" alt="image" src="https://user-images.githubusercontent.com/22605641/216855320-bad0c6f3-07bf-4202-baba-512396e8b703.png">
- [ ] Add a nice readme like what I have in the [streamlit version](https://github.com/rungalileo/bulk-labeling) - We should wait until the visual issues are fixed so we don't need to redo it 
- [ ] Write the blog on how I built it (same as above, wait until it's in a better state)
- [ ] Deploy on solara cloud?!? 🚀
