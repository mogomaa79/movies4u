from util import get_recommendations
from models import Film

print([Film.objects.get(id=i) for i in get_recommendations([12])])