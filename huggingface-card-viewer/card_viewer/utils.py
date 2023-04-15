import reacton.ipyvuetify as v
import solara as sl


def format_readme(readme: str):
    """Format the metadata within a readme as a scrollable window

    The only reason this function is complex is because I want to strip out the
    metadata from the card. It's at the top of the file and can be really long and
    ugly. It can take up the full screen (see `wikipedia`) and ruins the experience
    ex:
      ---
      text
      text
      text
      text
      text
      ...
      ---
      # Dataset Card
      ...

    We want to make that area scrollable and move it to the bottom so it doesn't
    take up so much space
    """
    card_md = v.Container(style_="height: 700px; overflow-y: scroll;")
    # Strip out the newlines, just get the metadata and card content
    content = [i.strip() for i in readme.split("---", 2) if i]
    if len(content) == 2:
        meta, card = content
        # First add the card content
        card_md.add_children([sl.Markdown(card)])

        # Create a small, scrollable container for metadata
        meta_md = v.Container(style_="height: 150px; overflow-y: scroll;")
        # Add the metadata at the bottom
        card_md.add_children([sl.Markdown("### Metadata")])
        meta_md.add_children([sl.Markdown(meta)])
        card_md.add_children([meta_md])
    else:
        # There's no metadata, just add the readme Markdown
        card = content[0]
        card_md.add_children([sl.Markdown(card)])
    return card_md
