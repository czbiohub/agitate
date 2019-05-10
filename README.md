# agitate
Use the power of a remote dev server with the lightness of local laptop editing.


# installation

`pip install 'git+git://github.com/czbiohub/agitate.git'`


# usage

   on dev server:

```
        git clone <some_repo>
        cd <repo>
```

   on laptop:

```
        git clone <same_repo>
        cd <repo>
        git checkout -b "my_work_in_progress" origin/master
        agitate ubuntu@<dev_server>:<repo>
```

   The `agitate` process continuously watches the laptop repo for changes.  As soon as a file is added or modified, `agitate`
   pushes the change to github and to the dev server, then runs `make` on the devserver to reveal
   syntax errors in near realtime (provided a Makefile is present).

   When work reaches a meaningful milestone, or a state that may be worth reverting to:
   CTRL-C the `agitate` process, amend its autosave commit with a more descriptive
   message, and restart.

   It is possible to omit `ubuntu@` and even `:<repo>` from the agitate command, provided the remote repo
   is located in the remote user's home dir.  The command becomes simply
```
    agitate <dev_server>
```


# caution

   1. USE AT YOUR OWN RISK.  The `agitate` monitor force-pushes to github in order to update
      its autosave commit every time it detects a change.  This is usually the
      desired behavior, but may surprise some and cause data loss.

   2. DO NOT INVOKE CONCURRENTLY ON THE SAME BRANCH.


# tips

For faster saving consider using SSH instead of HTTPS
in cloning your GIT repo, then implement the following
technique for speeding up SSH session creation:
https://developer.rackspace.com/blog/speeding-up-ssh-session-creation/


# see also

The comment at top of [scripts/agitate](scripts/agitate), and read the code.
