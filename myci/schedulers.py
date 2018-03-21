from buildbot.plugins import (
    schedulers,
    util
)

# Configure the Schedulers, which decide how to react to incoming changes.  In this
# case, just kick off a 'runtests' build

def get_schedulers():
    return [
        schedulers.SingleBranchScheduler(
            name="all",
            change_filter=util.ChangeFilter(branch='master'),
            treeStableTimer=None,
            builderNames=["runtests"]),
        schedulers.ForceScheduler(name="force", builderNames=["runtests"])
    ]
