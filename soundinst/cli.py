import argparse

from soundinst.inst import play, list_ports


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', type=str, help='command to execute')
    parser.add_argument('--dir', type=str, help='directory with audio files', default='audio')

    args = parser.parse_args()

    # execute command
    if args.command == 'play':
        play(args.dir)
    elif args.command == 'ports':
        list_ports()
    else:
        print('Unknown command: {}'.format(args.command))
