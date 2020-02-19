import argparse
import sys
import os
from cookiecutter.main import cookiecutter

def main():
    parser = argparse.ArgumentParser("Run docker project migrator")
    parser.add_argument("-s","--source_dir", help="Parent directory of current docker repository", required=True)
    args = parser.parse_args()
    os.chdir(args.source_dir + '/docker')
    [cookiecutter('/home/cisz/git/tomtom/github/gradle_cookiecutter/', \
        extra_context={'directory_name':'docker_' + o, 'pipeline_name': 'docker_' + o, 'pipeline_description': 'Description for pipeline ' + o }) \
        for o in os.listdir('.') if os.path.isdir(o)]

if __name__ == "__main__":
    sys.exit(main())