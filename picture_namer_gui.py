from gooey import Gooey, GooeyParser
import picture_namer


# Project GitHub URL
github_url = 'https://github.com/sky5hr0ud/picture_namer'


@Gooey(
    program_name='picture_namer',
    program_description='Prepends the directory name to pictures.',
    default_size=(1280, 720),
    image_dir='./images',
    show_restart_button=False,
    menu=[{'name': 'File', 'items': [{
        'type': 'Link',
        'menuTitle': 'Visit Website',
        'url': github_url
    }, {
        'type': 'Link',
        'menuTitle': 'Latest Filetypes File',
        'url': github_url + '/blob/master/_list_of_filetypes.txt',
    }, {
        'type': 'AboutDialog',
        'menuTitle': 'About',
        'name': 'picture_namer',
        'description': 'Prepend the directory name to your pictures',
        'version': '1.0.2',
        'copyright': '2022',
        'website': github_url,
        'developer': 'sky5hr0ud',
        'license': 'GPL-3.0'
    }]
    }])
def main():
    parser = GooeyParser()
    user_input = False
    required_args = parser.add_argument_group('Required Input')
    optional_args = parser.add_argument_group('Options')
    required_args.add_argument(
        '--Folderpath', type=str,
        help='Add a path to the folder containing images', widget='DirChooser')
    optional_args.add_argument(
        '--Filename', help='Sort by filename instead of date modified',
        action='store_true')
    optional_args.add_argument(
        '-e', '--Explicit', help='Ignore letter case in filetypes',
        action='store_false')  # We want this checked on the GUI
    optional_args.add_argument(
        '-l', '--List', type=str, help='Use a custom list of filetypes',
        widget='FileChooser')
    args = parser.parse_args()
    modified_sort = not args.Filename
    # Need to negate args.Explicit since we wanted this checked in GUI
    explicit = not args.Explicit
    filetypes_options = [False, args.List, explicit]
    if args.List:
        filetypes_options[0] = True
    try:
        picture_namer.file_namer(args.Folderpath, args.Filename, modified_sort,
                                 user_input, filetypes_options)
    except Exception as e:
        print(e)
    return 0


if __name__ == '__main__':
    main()
