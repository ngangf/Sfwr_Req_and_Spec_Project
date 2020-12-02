from Project.profile import Profile
from Project.order import Order


def test_add_points_to_profile_for_orders_above_10_dollars():
    profile = Profile()
    assert len(profile) == 0, "the profile should start with no reward points"

    price = Order()
    calculated_price = price.calculate_order(10)

    assert calculated_price == 10
    assert len(profile) == 10, "the profile should now have 10 reward points"

def test_add_points_to_profile_for_orders_below_10_dollars():
    profile = Profile()
    assert len(profile) == 0, "the profile should start with no reward points"

    price = Order()
    calculated_price = price.calculate_order(5)

    assert calculated_price == 5
    assert len(profile) == 0, "No reward points should be added to the profile"

def test_redeem_reward_at_60_points():
    profile = Profile()

    if len(profile) == 60: # If the profile has 60 reward points
        message = ('Click the Redeem icon below to get a free dinner option')
        print(message)

    else:
        message = ('You need more points to get a free dinner option')
        print(message)


