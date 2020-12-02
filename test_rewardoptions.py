from Project.rewardmenu import RewardMenu

def test_valid_menu_for_rewards():
    valid_menu = [
        "hamburger",
        "pizza",
        "fried chicken",
    ]

    reward = RewardMenu()
    for menu in valid_menu:
        assert reward.verify_menu(menu) == True, "Reward menu should be verified as valid"

def test_invalid_menu_for_rewards():
    invalid_menu = [
        "salad",
        "smoothie",
        "drinks",
        "dessert",
    ]

    reward = RewardMenu()
    for menu in invalid_menu:
        assert reward.verify_menu(menu) == False, "Reward menu should not be verified, it is false"
