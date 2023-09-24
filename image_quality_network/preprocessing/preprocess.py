import os
import argparse


def preprocess()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Preprocessing of fundus images')
    parser.add_argument('--data_dir', help='Directory where Eyepacs images are stored', type=str, required=True)
    parser.add_argument('--save_dr', help='Where to store the image', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    preprocess(**vars(args))
