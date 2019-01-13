from channels_api.bindings import ResourceBinding

from .models import RandomNum
from .serializers import RandomNumSerializer
import random
class RandomBinding(ResourceBinding):

    model = RandomNum
    stream = "random"
    serializer_class = RandomNumSerializer
    queryset = RandomNum.objects.all()