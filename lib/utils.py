from os import rename

def set_indexes_in_filenames(filepaths):
    filepaths_split = [x.rpartition('/') for x in filepaths]

    folderpaths, filenames = [], []
    for x in filepaths_split:
        folderpaths.append(x[0])
        filenames.append(x[2])
    
    n_videos = len(filenames)
    n_digits_index = len(str(n_videos))
    new_filenames = filenames

    for i in range(n_videos):
        n_zeros = n_digits_index-len(str((i+1)))
        new_filenames[i] = "0"*n_zeros + f"{i+1} - " + new_filenames[i]

    for i in range(n_videos):
        rename(filepaths[i], '/'.join([folderpaths[i], new_filenames[i]]))