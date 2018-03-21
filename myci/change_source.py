from buildbot.plugins import changes

# the 'change_source' setting tells the buildmaster how it should find out
# about source code changes.  Here we point to the buildbot version of a python hello-world project.

def get_change_source():
    return [
        changes.GitPoller(
            'git://github.com/buildbot/hello-world.git',
            workdir='gitpoller-workdir', branch='master',
            pollinterval=300)
    ]
