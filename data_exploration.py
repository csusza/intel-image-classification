from pathlib import Path
from random import shuffle

from matplotlib import pyplot as plt

if __name__ == '__main__':
    data_path = {'train': Path('data/seg_train/seg_train'),
                 'test': Path('data/seg_test/seg_test'),
                 'pred': Path('data/seg_pred/seg_pred'), }

    classes = [path.name for path in data_path['train'].glob('*')]
    print(f'Number of classes: {len(classes)}\n'
          f'Classes in the dataset: {classes}\n')

    num_images = {'train': len(list(data_path['train'].rglob('**/*.jpg'))),
                  'test': len(list(data_path['test'].rglob('**/*.jpg'))),
                  'pred': len(list(data_path['pred'].rglob('**/*.jpg'))), }
    for category in num_images:
        print(f'Number of {category} images: {num_images[category]}')

    num_by_category = dict()
    for category in classes:
        num_images = len(list(data_path['train'].rglob(f'{category}/*.jpg')))
        num_by_category[category] = num_images
    print(f'\nIn the training set there are: ')
    for category, value in num_by_category.items():
        print(f'{value} {category} images,')

    if min(num_by_category.values()) / min(num_by_category.values()) > .85:
        print(f'The dataset is balanced.')
    else:
        print(f'The dataset is unbalanced.')

    train_img_paths = list(data_path['train'].rglob('**/*.jpg'))
    shuffle(train_img_paths)

    print(f'\nShow few images from the training set:')
    n_rows = 6
    n_cols = 6
    fig = plt.figure(figsize=(20, 20))
    gs = fig.add_gridspec(n_rows, n_cols, hspace=0, wspace=0)
    sp = gs.subplots(sharex=True, sharey=True)
    for i in range(n_rows):
        for j in range(n_cols):
            image_path = train_img_paths[n_rows * i + j]
            sp[i, j].imshow(plt.imread(image_path))
            sp[i, j].set_axis_off()
            sp[i, j].text(8, 14, f'{image_path.parent.name}',
                          bbox={'facecolor': 'white', 'pad': 10},
                          fontsize=14)
    plt.show()
