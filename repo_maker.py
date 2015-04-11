from gitlab import Gitlab
from os import environ as ENV
from argparse import ArgumentParser


def wedontgoto25120152(group, team):
    if group == 4 and team >= 2:
        return team + 1
    else:
        return team


def createproject(git, group, team, namespace=None):
    team = wedontgoto25120152(group, team)

    group_name = hex(group)[2:].upper()
    team_name = "team%s%i" % (group_name, team)

    if namespace:
        namespace_id = next(group for group in git.getgroups()
                            if group["path"] == namespace)["id"]
        created = git.createproject(team_name, namespace_id=namespace_id)
    else:
        created = git.createproject(team_name)

    if created:
        print("Created %s%s" % (namespace + "/" if namespace else "", team_name))
    else:
        print("Error creating %s%s" % (namespace + "/" if namespace else "",
                                       team_name))


def main(args):
    num_groups = int(args.num_groups)
    num_teams = int(args.num_teams)
    namespace = args.namespace

    git = Gitlab(args.host, token=ENV["gl_token"])

    for group in range(1, num_groups + 1):
        for team in range(1, num_teams + 1):
            createproject(git, group, team, namespace)

if __name__ == "__main__":
    parser = ArgumentParser(
        description="cr3473 pr0pr4 r3p05 w17h l337 numb3r1n6")
    parser.add_argument("host", metavar="HOST",
                        help="The server where gitlab is hosted")
    parser.add_argument("num_groups", metavar="GROUPS",
                        help="Number of groups per week")
    parser.add_argument("num_teams", metavar="TEAMS",
                        help="Number of teams per group")
    parser.add_argument("-n", "--namespace", help=(
        "Namespace to create the project in. Defaults to the users namespace"))

    main(parser.parse_args())
