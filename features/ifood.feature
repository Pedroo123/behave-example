Feature: Testing ifood landing page

Scenario: Visit ifood and type my location
Given I am on ifood page "https://www.ifood.com.br/lista-restaurantes"
When I type my address
Then My location should be shown on the modal
