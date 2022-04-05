import typer
from ssg.site import Site

def main(source="content", dest="dist"):
    config = {"source" : source, "dest" : dest}
    instance = Site(config["source"], config["dest"])
    instance.build()

typer.run(main)
