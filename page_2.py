import panel as pn
pn.extension()

def view():
    return pn.Column("# Page 2", "This is Page 2.")

pn.panel(view).servable()
