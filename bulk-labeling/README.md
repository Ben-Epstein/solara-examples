# bulk-labeling-solara
A tool for bulk labeling, built in Solara!

I'm trying to rebuild my original [bulk-labeling](https://github.com/rungalileo/bulk-labeling/) app, which was Streamlit, in [Solara](https://github.com/widgetti/solara) so it can be a bit more scalable, customizable, and robust to new features!

I also want to learn how to use solara :)

## How to use
We can walk through a simple example of going from an unlabeled dataset to some usable labels in just a few minutes.

First, [run the app locally](https://github.com/Ben-Epstein/solara-examples/blob/main/bulk-labeling/CONTRIBUTING.md#development) (Cloud deployment coming soon!)

Then upload a csv file with your text. The only requirement of the file is that it must have a text column. Any other columns added can be used for coloring the embedding plot. If you don't have one, you can use the [conv-intent](https://github.com/Ben-Epstein/solara-examples/blob/main/bulk-labeling/bulk_labeling/conv_intent.csv) dataset from this repo!

![image](https://github.com/Ben-Epstein/solara-examples/assets/22605641/102f2931-ef83-4c2d-b92c-97cc2b25f0cd)

Once the embeddings have processed, you'll see your dataframe on the left and embeddings on the right. The dataframe view comes with an extra text_length column that you can sort by, or color the embeddings plot with (in case text length is useful to you).

You can filter with the text search (regex coming soon!) or, by lasso selecting embedding clusters from the chart. You can also color the chart and resize the points using the menu on the left.

![image](https://github.com/Ben-Epstein/solara-examples/assets/22605641/8add7a83-1739-45cc-a441-6f29dcc7d08b)



### Roadmap
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
