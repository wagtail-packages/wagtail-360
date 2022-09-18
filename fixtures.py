import subprocess
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    fixtures = base_dir / "wagtail_360/test/fixtures" / "fixtures.json"

    if not fixtures.exists():
        dump_command = f"python manage.py dumpdata --natural-foreign --indent 2 \
        -e contenttypes -e auth.permission \
        -e wagtailcore.groupcollectionpermission \
        -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
        -e sessions > {fixtures}"
        subprocess.run(dump_command, shell=True, check=True)
    else:
        print("Fixtures already exist")


if __name__ == "__main__":
    main()
