from buildbot.plugins import worker


# The 'workers' list defines the set of recognized workers. Each element is
# a Worker object, specifying a unique worker name and password.  The same
# worker name and password must be configured on the worker.



def get_workers():
    """
    Entrypoint to configure the workers in the Master.

    Return a list of Workers.
    """
    return [
        worker.LocalWorker("default"),
        worker.LocalWorker("worker-1"),
        worker.LocalWorker("worker-2"),
        worker.LocalWorker("worker-3"),
        worker.LocalWorker("worker-4")
    ]
