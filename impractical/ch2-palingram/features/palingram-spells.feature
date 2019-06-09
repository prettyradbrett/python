
Feature: Palingram Spell Generator

   As a lover of language
   I would like a program to generate multi word palingrams
   So that I can enjoy having built a goofy program

   
   Scenario: User requests a palingram
      Given the server is available
      When the user requests a palingram
      Then the system returns a multi-word phrase
      And it is identical when all characters are reversed
      And it is unique for each request
      And it starts with the text "Jeff"

   @other @wip
   Scenario: User submits a post to the service
      Given the server is available
      When the user submits a post
      Then the system returns an error code