import panel as pn
pn.extension()

def view():
    return pn.Column("# Page 1", "This is Page 1.")

pn.panel(view).servable()
