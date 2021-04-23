global track
global track_list
track_list = []


class Track:
    def __init__(self):
        self.title = None
        self.artists_or_album = None

    def set_track_info(self, _title, _artists_or_album):
        if _title == None and _artists_or_album == None:
            log.debug("No info found")
        else:
            self.title = _title
            self.artists_or_album = _artists_or_album
            # self.album = info['album']

    def get_track_title(self):
        return self.title

    def clear_info(self):
        self.title = None
        self.artists_or_album = None

        # self.album = None

    def append_to_list(self):
        pass
        # global track_list
        # track_list.append(self)
        # print(track_list)

        # found = False
        # for index in range(0, len(track_list)):
        #     if self.title == track_list[index]['title']
        #         found = True
        # if not found:
        #     track_list.append(self)


track = Track()
