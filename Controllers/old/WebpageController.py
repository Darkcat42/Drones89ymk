from Models.Webpages import Webpage
class WebpageController():
    @ classmethod
    def add_link(cls):
        pass
    @ classmethod
    def get_links_order_by_pos(cls):
        return Webpage.select().order_by(Webpage.position, 'asc')
    @ classmethod
    def add_link(cls, name, url, type_link, position):
        return Webpage.create(
            name=name,
            url=url,
            type=type_link,
            position=position
        )
    @classmethod
    def delete(cls, id):
        Webpage.delete().where(Webpage.id == id).execute()
    @classmethod
    def get_by_url(cls, url):
        return Webpage.get_or_none(Webpage.url == url)
    @classmethod
    def get_order_by_webpages(cls):
        list_webpages = cls.get_links_order_by_pos()
        webpage_links = []
        for webpage_obj in list_webpages:
            link = []
            link.append(webpage_obj.name)
            link.append(webpage_obj.url)
            link.append(webpage_obj.id)
            webpage_links.append(link)
        return webpage_links


