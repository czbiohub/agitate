# agitate
Devtools blending the power of remote dev servers with the lightness of local laptop editing.


# installation

`pip install 'git+git://github.com/czbiohub/agitate.git'`


# usage

   on dev server:

```
        ssh ubuntu@<dev_server>
        git clone <some_repo>
        cd <repo>
```

   on laptop:

```
        git clone <same_repo>
        cd <repo>
        git checkout -b "work_in_progress" origin/master
        agitate ubuntu@<dev_server>:<repo>
```

   This will monitor locally on the laptop for changes to
   any files in git.  It will autosave/autopush any changes using the
   current branch that is checked out on the laptop, squashing
   all changes into an automatically created autosave commit.  That
   will be pushed both to github and to the specified dev server SSH
   coordinates.  If there is a Makefile, it will be executed on
   the dev server.  This is convenient for getting realtime feedback
   on C++ or Go syntax errors, as you fix them in your laptop editor.

   When your work reaches a meaningful milestone, CTRL-C the agitate
   monitor, edit the autosave commit message to something more useful,
   then restart the monitor.


# cautions

   When it starts up, agitate will force-push to github the current top
   commit IF THERE ARE NO ADDED OR MODIFIED FILES.  This is usually the
   desired behavior, but under some circumstances it might overwrite
   or lose data in github contrary to a user's wishes.  Use at your own
   risk.

   DO NOT INVOKE CONCURRENTLY ON THE SAME BRANCH

# see also

The comment at top of [scripts/agitate](scripts/agitate) list other important information.
