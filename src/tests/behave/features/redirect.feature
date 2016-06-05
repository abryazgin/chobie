Feature: Redirecting

  Scenario Outline: Incorrect subURLs must redirected to main
     Given Nothing
      When I go to '<suburl>'
      Then Redirected
       And I have redirected to 'main' page

   Examples: incorrect URLs
     | suburl                           |
     | /                                |
     | /some/incorrect/path/            |
     | /112133/12312fsdfsdf/sdf*&T*FGV/ |
     | /main/12312fsdfsdf/sdf*&T*FGV/   |
