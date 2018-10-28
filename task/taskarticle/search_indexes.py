import datetime
from haystack import indexes
from taskarticle.models import  ArticleInfo

class ArticleInfoIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)

    author=indexes.CharField(model_attr='author')

    title=indexes.CharField(model_attr='title')

    content=indexes.CharField(model_attr='content')

    time=indexes.CharField(model_attr='add_time')

    def get_model(self):
        return ArticleInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
    # 这就是  model  上一部 在 setting里加入了  配置信息
    # class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    #     text = indexes.CharField(document=True, use_template=True)
    #
    #     author = indexes.CharField(model_attr='user')
    #     pub_date = indexes.DateTimeField(model_attr='pub_date')
    #
    #     def get_model(self):
    #         return Note
    #
    #     def index_queryset(self, using=None):
    #         """Used when the entire index for model is updated."""
    #         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())