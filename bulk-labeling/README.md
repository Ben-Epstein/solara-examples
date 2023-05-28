# bulk-labeling
A tool for bulk labeling, built in Solara!

<img width="1675" alt="image" src="https://github.com/Ben-Epstein/solara-examples/assets/22605641/1d96c594-90fc-40dc-b497-88e4965fcbea">


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

Since we see some clear clusters already, let's start by investigating them. We can see one cluster with a lot of references to weather. Let's select this cluster

https://github.com/Ben-Epstein/solara-examples/assets/22605641/09d4da1a-cc56-4580-bbc5-e5d1240ba971

Confirming that this is about weather, we can register a new label "weather" and assign our samples

https://github.com/Ben-Epstein/solara-examples/assets/22605641/90c1fece-d8a7-4d7c-97f1-4c69fee372c0

The UI will reset automatically. Let's look at another one. This cluster has a lot of references to bookings and reservations. Let's select that one.

https://github.com/Ben-Epstein/solara-examples/assets/22605641/52a6a970-33fb-4df2-9458-77f69ec459bf


Once we are ready, we simple click "Export Labeled Points"

![image](https://github.com/Ben-Epstein/solara-examples/assets/22605641/8d845410-d644-4d39-838b-392ea2538937)

We just labeled N samples in a few minutes!

There are some pretty funny "mistakes" in the embeddings (samples that are semantically similar to other categories, but have words that trigger weather/reservation) that should be considered! The embeddings aren't perfect. We are using a smaller model (paraphrase-MiniLM-L3-v2) in order to get embeddings in a reasonable speed. But it's a good start! Feel free to run this locally and use a better model

![image](https://github.com/Ben-Epstein/solara-examples/assets/22605641/74b10ae5-afcf-4d49-a6bc-bda310d56d77)

## Run locally

If you have a GPU running locally, want to try different encoder algorithms, or don't want to upload your data, you can run this locally.
```
pip install -r requirements.txt
solara run bulk_labeling/main.py
```


### Roadmap
- [X] Allow the user to download the labeled file :D (https://github.com/widgetti/solara/pull/30)
- [X] Fix the layout of embeddings and dataframe so they are next to each other (not stacked)
- [X] Use `solara.progress` for UMAP
- [X] Remove `.use` from the code
- [X] Camel Case my components
- [X] Move to the new `solara.reactive`
- [ ] Get a more fun animation for when the embeddings are being calculated. Would also be cool if we could update them with the logs from UMAP or tqdm
- [ ] The "reset filters" button should really be a switch, not a checkbox. It doesn't look great<br> <img width="288" alt="image" src="https://user-images.githubusercontent.com/22605641/216855320-bad0c6f3-07bf-4202-baba-512396e8b703.png">
- [X] Add a nice readme like what I have in the [streamlit version](https://github.com/rungalileo/bulk-labeling)
- [ ] Write the blog on how I built it (same as above, wait until it's in a better state)
- [ ] Deploy on solara cloud?!? 🚀
