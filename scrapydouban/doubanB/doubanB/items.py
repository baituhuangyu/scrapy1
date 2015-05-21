from scrapy.item import Item, Field
 
class DoubanItem(Item):
    # define the fields for your item here like:
    # name = Field()
    groupName = Field()
    groupURL = Field()
    totalNumber = Field()
    RelativeGroups = Field()
    ActiveUesrs = Field()
