import argparse


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', type=str, help='command to execute')
    parser.add_argument('--dir', type=str, help='directory with audio files', default='audio')

    args = parser.parse_args()

    # execute command
    if args.command == 'play':
        # args.dir
        pass
    else:
        print('Unknown command: {}'.format(args.command))
