from helpers import api


class Downloader:
    URL = 'http://202.90.198.22/IMAGE/HOTSPOT/%s/%s/hotspot_%s.txt'
    def __init__(self, builder):
        self.year = builder.y
        self.month = builder.m
        self.day = builder.d
        self.result = None
        Downloader.URL = Downloader.URL % (self.year,
                                           self.month,
                                           self.year+self.month+self.day)

    @staticmethod
    class Init:
        def __init__(self):
            # set default value
            self.y = '2015'
            self.m = '01'
            self.d = '01'
            pass

        def year(self, vyear):
            self.y = vyear
            return self

        def month(self, vmonth):
            self.m = vmonth
            return self

        def day(self, vday):
            self.d = vday
            return self

        def build(self):
            return Downloader(self)

    def prompt(self):
        print "Downloaded from: "+Downloader.URL
        return self

    def download(self):
        data = api.get(Downloader.URL)
        self.result = self.parse(data)
        return self

    def parse(self, text):
        rows = text.split("\n")
        header = rows[0].split("\t")
        parsed = []
        for i in xrange(0, len(rows)-1):
            data = rows[i+1].split("\t")
            d = dict()
            for j in xrange(0, len(data)-1):
                d.update({header[j]:data[j]})

            parsed.append(d)

        return parsed

Downloader.Init().year('2015').month('02').day('14').build().prompt().download()