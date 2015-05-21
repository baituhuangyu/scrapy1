from scrapy.item import Item, Field

class MaizieduItem(Item):
    pageName = Field()
    pageURL = Field()
    
    courseName = Field()
    courseURL = Field()
    
    academicName = Field()
    academicURL = Field()

    bbsName = Field()
    bbsURL = Field()

    appName = Field()
    appURL = Field()
   
    teacherName = Field()
    teacherCourse = Field()
    teacherCourseURL = Field()
    teacherIntroduction = Field()

    aboutName = Field()
    aboutURL = Field()
