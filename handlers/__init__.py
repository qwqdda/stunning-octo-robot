from .start import register_start
from .ad import register_ad
from .balance import register_balance
from .referral import register_referral

def register_handlers(dp):
    register_start(dp)
    register_ad(dp)
    register_balance(dp)
    register_referral(dp)
