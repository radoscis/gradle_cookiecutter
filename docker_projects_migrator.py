import argparse
import sys
import os
from cookiecutter.main import cookiecutter

def main():
    parser = argparse.ArgumentParser("Run docker project migrator")
    parser.add_argument("-s","--source_dir", help="Parent directory of current docker repository", required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-g","--github_url", help="Cookiecutter template repo from github")
    group.add_argument("-d","--local_dir", help="Cookiecutter template repo from local directory")
    args = parser.parse_args()
    os.chdir(args.source_dir + '/docker')
    if args.github_url:
        [cookiecutter(args.github_url, \
            extra_context={'directory_name':'docker_' + subdir, 'pipeline_name': 'docker_' + subdir, 'pipeline_description': 'Description for pipeline ' + subdir }) \
            for subdir in os.listdir('.') if os.path.isdir(subdir)]
    if args.local_dir:
        [cookiecutter(args.local_dir, \
            extra_context={'directory_name':'docker_' + subdir, 'pipeline_name': 'docker_' + subdir, 'pipeline_description': 'Description for pipeline ' + subdir }) \
            for subdir in os.listdir('.') if os.path.isdir(subdir)]

if __name__ == "__main__":
    sys.exit(main())