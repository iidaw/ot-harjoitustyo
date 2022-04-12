from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True) #toimii

@task
def test(ctx):
    ctx.run("pytest src", pty=True) #toimii

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True) #toimii

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True) #toimii

@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=True)

#tähän pitäis saada yhdistys tietokantaan!!
@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True) #toimii ehkä

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
    