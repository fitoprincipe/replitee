import ee
from auth import Initialize
Initialize()

print(ee.Image(0).getInfo())
