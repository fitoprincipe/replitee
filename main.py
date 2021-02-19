import ee
from auth import initialize
initialize()

print(ee.Image(0).getInfo())