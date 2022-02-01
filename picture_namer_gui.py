from gooey import Gooey, GooeyParser
import picture_namer


@Gooey(
    program_name='picture_namer',
    program_description='Prepends the directory name to pictures.',
    show_restart_button=False,
    menu=[{'name': 'File', 'items': [{
        'type': 'Link',
        'menuTitle': 'Visit Website',
        'url': 'https://github.com/sky5hr0ud/picture_namer'
    }, {
        'type': 'AboutDialog',
        'menuTitle': 'About',
        'name': 'picture_namer',
        'description': 'Prepend the directory name to your pictures',
        'version': '1.0.2',
        'copyright': '2022',
        'website': 'https://github.com/sky5hr0ud/picture_namer',
        'developer': 'https://github.com/sky5hr0ud',
        'license': 'GPL-3.0'
    }]
    }])
def main():
    parser = GooeyParser()
    required_args = parser.add_argument_group('Required Input')
    optional_args = parser.add_argument_group('Options')
    optional_args.add_argument(
        '--Filename', help='Sort by filename instead of date modified',
        action='store_true')
    required_args.add_argument(
        '--Folderpath', type=str,
        help='Add a path to the folder containing images', widget='DirChooser')
    args = parser.parse_args()
    if args.Filename is True:
        filename_sort = True
        modified_sort = False
    else:
        filename_sort = False
        modified_sort = True
    try:
        picture_namer.file_namer(args.Folderpath, filename_sort, modified_sort)
    except Exception as e:
        print(e)
    return 0


if __name__ == '__main__':
    main()
