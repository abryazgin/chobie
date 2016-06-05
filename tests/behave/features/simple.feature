Feature: simple

  Scenario: Test our testing library
    Given Nothing
    When Run a passing step
    Then Everything is fine

  Scenario: Тестируем кириллические сценарии
    Given У нас есть steps с русскими символами
    When Когда мы запускаем какой-нибудь из них
    Then Ничего не ломается!