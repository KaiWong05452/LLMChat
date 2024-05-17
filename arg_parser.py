import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='API Server Configuration')
    parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the API on')
    args = parser.parse_args()
    return args
