from yt_dlp.postprocessor.common import PostProcessor

class FilenameExtractorPP(PostProcessor):
    def __init__(self):
        super(FilenameExtractorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information['filepath'])
        return [], information