from buildbot.plugins import (
    util,
    steps
)
# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which workers can execute them.  Note that any particular build will
# only take place on one worker.


def get_builders():
    factory = util.BuildFactory()
    # check out the source
    factory.addStep(
        steps.Git(repourl='git://github.com/buildbot/hello-world.git',
                  mode='incremental'))
    # run the tests (note that this will require that 'trial' is installed)
    factory.addStep(
        steps.ShellCommand(command=["trial", "hello"],
                           env={"PYTHONPATH": "."}))
    return [
        util.BuilderConfig(name="runtests",
                           workernames=["default"],
                           factory=factory)
    ]
