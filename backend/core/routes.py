from rest_framework.routers import DefaultRouter, SimpleRouter
from landlord.views import LandLordViewset
from place.views import PlaceViewset
from opening_hours.views import Opening_HoursViewset
from payment.views import  PaymentViewset
from rent.views import RentViewset
from authentication.views import UserViewset

router=DefaultRouter()


router.register('landlord', LandLordViewset )
router.register('place', PlaceViewset )
router.register('opening_hours', Opening_HoursViewset )
router.register('payment', PaymentViewset )
router.register('rent', RentViewset )
router.register('auth', UserViewset )