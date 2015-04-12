# repo-maker

This is a tool to create a bunch of repositories in gitlab. One can pass a number of groups and a
number of teams per group and this tools creates repositories with names like `teamXY` where `X` is
the group number in hex (i.e. 1, 2, 3, ..., 9, A, ..., F, 10, 11, 12, ....) and `Y` simply the team
number. There is no `team42`\*!

Optionally one can put the project into a namespace (i.e. group) from gitlab. Just pass the path
of the group as `NAMESPACE` parameter to the tool.


\* [We don't go to 25.12.01.52](http://wedontgoto25120152.de)

## Usage

```
python repo_maker.py -h
usage: repo_maker.py [-h] [-n NAMESPACE] GROUPS TEAMS
```

## Authentication

This tool uses token authentication. Set up an api token for your gitlab account and export it as
`gl_token` in your shell before running the tool.

```
export gl_token=FFFACAB666
python repo-manager 15 7
```

A `token` file is ignored in `.gitignore` for convenience. You can store the token there.

```
export gl_token=`cat token`
python repo-manager 15 7
```
