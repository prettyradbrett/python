
Feature: Anagram Solver

   As a lover of word puzzles
   I would like a tool to find anagrams for a given word or name
   So that I can quickly solve jumble puzzles and impress my friends

   
   Scenario Outline: Getting anagrams of <keyword>
      Given the server is available
      When I input <keyword>
      Then the result should contain <result>

   Examples:
   | keyword | result |
   | "Listen" | "Silent" |
   | "Brag" | "Grab" |
   | "Cat" | "Act" |
   | "Fx" | "No Results" |

   @other @wip
   Scenario: User submits a post to the service
      Given the server is available
      When the user submits a post
      Then the system returns an error code