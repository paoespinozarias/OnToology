
class FakeRequest():
    def __init__(self):
        self.POST={}



def get_fake_webhook_ontology_change_request(repo='usertest/testrepo',email='test@mail.com',msg='Testing Default Message'):
    request=FakeRequest()
    request.POST['payload'] = """
{
  "ref": "refs/heads/master",
  "before": "c35a93d7fd4added59283c8fcd4235b1a8ea02c1",
  "after": "1fb6e048f31d0a7f4afa4ae5517e486a5a204160",
  "created": false,
  "deleted": false,
  "forced": false,
  "base_ref": null,
  "compare": "https://github.com/ahmad88me/target/compare/c35a93d7fd4a...1fb6e048f31d",
  "commits": [
    {
      "id": "e263f40054a91364932029be2409b79286405c5d",
      "distinct": true,
      "message": "automated change",
      "timestamp": "2015-05-11T00:55:50Z",
      "url": "https://github.com/ahmad88me/target/commit/e263f40054a91364932029be2409b79286405c5d",
      "author": {
        "name": "AutonUser",
        "email": "ahmad88csc@gmail.com",
        "username": "AutonUser"
      },
      "committer": {
        "name": "AutonUser",
        "email": "ahmad88csc@gmail.com",
        "username": "AutonUser"
      },
      "added": [

      ],
      "removed": [

      ],
      "modified": [
        "auton/org/daniel.owl/auton.cfg",
        "auton/org/daniel.owl/diagrams/ar2dtool-class/daniel.owl.png",
        "auton/org/daniel.owl/diagrams/ar2dtool-class/daniel.owl.png.dot",
        "auton/org/daniel.owl/diagrams/ar2dtool-class/daniel.owl.png.graphml",
        "auton/org/daniel.owl/diagrams/ar2dtool-taxonomy/daniel.owl.png",
        "auton/org/daniel.owl/diagrams/ar2dtool-taxonomy/daniel.owl.png.dot",
        "auton/org/daniel.owl/diagrams/ar2dtool-taxonomy/daniel.owl.png.graphml",
        "auton/org/daniel.owl/diagrams/config/ar2dtool-class.conf",
        "auton/org/daniel.owl/diagrams/config/ar2dtool-taxonomy.conf",
        "auton/org/daniel.owl/documentation/daniel.owl.widoco.conf",
        "auton/org/daniel.owl/documentation/index.html",
        "auton/org/daniel.owl/documentation/provenance/provenance.html",
        "auton/org/daniel.owl/documentation/provenance/provenance.ttl",
        "auton/org/daniel.owl/documentation/resources/extra.css",
        "auton/org/daniel.owl/documentation/resources/jquery.js",
        "auton/org/daniel.owl/documentation/resources/owl.css",
        "auton/org/daniel.owl/documentation/resources/primer.css",
        "auton/org/daniel.owl/documentation/resources/rec.css",
        "auton/org/daniel.owl/documentation/sections/abstract.html",
        "auton/org/daniel.owl/documentation/sections/crossref.html",
        "auton/org/daniel.owl/documentation/sections/description.html",
        "auton/org/daniel.owl/documentation/sections/introduction.html",
        "auton/org/daniel.owl/documentation/sections/overview.html",
        "auton/org/daniel.owl/documentation/sections/references.html",
        "auton/org/daniel.owl/oops/OOPSevaluation/evaluation/bootstrap.css",
        "auton/org/daniel.owl/oops/OOPSevaluation/evaluation/bootstrap.min.js",
        "auton/org/daniel.owl/oops/OOPSevaluation/evaluation/jquery-1.11.0.js",
        "auton/org/daniel.owl/oops/OOPSevaluation/evaluation/jquery.tablesorter.min.js",
        "auton/org/daniel.owl/oops/OOPSevaluation/evaluation/style.css",
        "auton/org/daniel.owl/oops/OOPSevaluation/oopsEval.html",
        "auton/org/daniel.owl/oops/index.html",
        "auton/org/daniel.owl/oops/provenance/provenance.html",
        "auton/org/daniel.owl/oops/provenance/provenance.ttl",
        "auton/org/daniel.owl/oops/resources/extra.css",
        "auton/org/daniel.owl/oops/resources/jquery.js",
        "auton/org/daniel.owl/oops/resources/owl.css",
        "auton/org/daniel.owl/oops/resources/primer.css",
        "auton/org/daniel.owl/oops/resources/rec.css",
        "auton/org/daniel.owl/oops/sections/abstract.html",
        "auton/org/daniel.owl/oops/sections/crossref.html",
        "auton/org/daniel.owl/oops/sections/description.html",
        "auton/org/daniel.owl/oops/sections/introduction.html",
        "auton/org/daniel.owl/oops/sections/overview.html",
        "auton/org/daniel.owl/oops/sections/references.html"
      ]
    },
    {
      "id": "1fb6e048f31d0a7f4afa4ae5517e486a5a204160",
      "distinct": true,
      "message": "Merge pull request #274 from AutonUser/master\n\nAutonTool update",
      "timestamp": "2015-05-11T02:53:38+02:00",
      "url": "https://github.com/ahmad88me/target/commit/1fb6e048f31d0a7f4afa4ae5517e486a5a204160",
      "author": {
        "name": "Ahmad Alobaid",
        "email": "ahmad88me@gmail.com",
        "username": "ahmad88me"
      },
      "committer": {
        "name": "Ahmad Alobaid",
        "email": "ahmad88me@gmail.com",
        "username": "ahmad88me"
      },
      "added": [

      ],
      "removed": [

      ],
      "modified": [

      ]
    }
  ],
  "head_commit": {
    "id": "1fb6e048f31d0a7f4afa4ae5517e486a5a204160",
    "distinct": true,
    "message": "%s",
    "timestamp": "2015-05-11T02:53:38+02:00",
    "url": "https://github.com/ahmad88me/target/commit/1fb6e048f31d0a7f4afa4ae5517e486a5a204160",
    "author": {
      "name": "Ahmad Alobaid",
      "email": "ahmad88me@gmail.com",
      "username": "ahmad88me"
    },
    "committer": {
      "name": "Ahmad Alobaid",
      "email": "ahmad88me@gmail.com",
      "username": "ahmad88me"
    },
    "added": [

    ],
    "removed": [

    ],
    "modified": [
      "org/daniel.owl",
      "alojamiento.owl"
    ]
  },
  "repository": {
    "id": 31723967,
    "name": "target",
    "full_name": "%s",
    "owner": {
      "name": "ahmad88me",
      "email": "%s"
    },
    "private": false,
    "html_url": "https://github.com/ahmad88me/target",
    "description": "sample for updates",
    "fork": false,
    "url": "Localtesting this is url",
    "forks_url": "https://api.github.com/repos/ahmad88me/target/forks",
    "keys_url": "https://api.github.com/repos/ahmad88me/target/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/ahmad88me/target/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/ahmad88me/target/teams",
    "hooks_url": "https://api.github.com/repos/ahmad88me/target/hooks",
    "issue_events_url": "https://api.github.com/repos/ahmad88me/target/issues/events{/number}",
    "events_url": "https://api.github.com/repos/ahmad88me/target/events",
    "assignees_url": "https://api.github.com/repos/ahmad88me/target/assignees{/user}",
    "branches_url": "https://api.github.com/repos/ahmad88me/target/branches{/branch}",
    "tags_url": "https://api.github.com/repos/ahmad88me/target/tags",
    "blobs_url": "https://api.github.com/repos/ahmad88me/target/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/ahmad88me/target/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/ahmad88me/target/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/ahmad88me/target/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/ahmad88me/target/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/ahmad88me/target/languages",
    "stargazers_url": "https://api.github.com/repos/ahmad88me/target/stargazers",
    "contributors_url": "https://api.github.com/repos/ahmad88me/target/contributors",
    "subscribers_url": "https://api.github.com/repos/ahmad88me/target/subscribers",
    "subscription_url": "https://api.github.com/repos/ahmad88me/target/subscription",
    "commits_url": "https://api.github.com/repos/ahmad88me/target/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/ahmad88me/target/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/ahmad88me/target/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/ahmad88me/target/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/ahmad88me/target/contents/{+path}",
    "compare_url": "https://api.github.com/repos/ahmad88me/target/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/ahmad88me/target/merges",
    "archive_url": "https://api.github.com/repos/ahmad88me/target/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/ahmad88me/target/downloads",
    "issues_url": "https://api.github.com/repos/ahmad88me/target/issues{/number}",
    "pulls_url": "https://api.github.com/repos/ahmad88me/target/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/ahmad88me/target/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/ahmad88me/target/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/ahmad88me/target/labels{/name}",
    "releases_url": "https://api.github.com/repos/ahmad88me/target/releases{/id}",
    "created_at": 1425573441,
    "updated_at": "2015-05-07T14:35:31Z",
    "pushed_at": 1431305619,
    "git_url": "git://github.com/%s",
    "ssh_url": "git@github.com:ahmad88me/target.git",
    "clone_url": "https://github.com/ahmad88me/target.git",
    "svn_url": "https://github.com/ahmad88me/target",
    "homepage": null,
    "size": 14958,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Web Ontology Language",
    "has_issues": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 1,
    "mirror_url": null,
    "open_issues_count": 1,
    "forks": 1,
    "open_issues": 1,
    "watchers": 0,
    "default_branch": "master",
    "stargazers": 0,
    "master_branch": "master"
  },
  "pusher": {
    "name": "ahmad88me",
    "email": "ahmad88me@gmail.com"
  },
  "sender": {
    "login": "ahmad88me",
    "id": 6922709,
    "avatar_url": "https://avatars.githubusercontent.com/u/6922709?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/ahmad88me",
    "html_url": "https://github.com/ahmad88me",
    "followers_url": "https://api.github.com/users/ahmad88me/followers",
    "following_url": "https://api.github.com/users/ahmad88me/following{/other_user}",
    "gists_url": "https://api.github.com/users/ahmad88me/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/ahmad88me/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/ahmad88me/subscriptions",
    "organizations_url": "https://api.github.com/users/ahmad88me/orgs",
    "repos_url": "https://api.github.com/users/ahmad88me/repos",
    "events_url": "https://api.github.com/users/ahmad88me/events{/privacy}",
    "received_events_url": "https://api.github.com/users/ahmad88me/received_events",
    "type": "User",
    "site_admin": false
  }
}
""" % (msg,repo,email,repo)
    return request

