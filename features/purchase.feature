Feature: Purchase
    """
        Login feature will test for successful and failed login attempts
    """

    Scenario: Success test for login
        Given I navigate to purchase page
        Then I see the Order Now text on the page

