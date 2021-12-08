Feature: Test BDD
  Scenario: Get roots of a biquadratic equation
    Given I give coefficients 4, -5, 1
    Then I get 1, -1, 0.5, -0.5 roots

    Given I give coefficients 1, -2, -8
    Then I get 2, -2 roots