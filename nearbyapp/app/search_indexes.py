from haystack import indexes
from api.models import Event


class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr='category', faceted=True)
    event_date = indexes.DateField(model_attr='event_date', faceted=True)

    def get_model(self):
        return Event

    def index_queryset(self, using=None):
        return self.get_model().objects.all()