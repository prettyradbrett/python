
Feature: Anagram Solver

   As a lover of word puzzles
   I would like a tool to find anagrams for a given word or name
   So that I can quickly solve jumble puzzles and impress my friends

   Scenario Outline: Getting single word anagrams of <keyword>
      Given the server is available
      When I input <keyword>
      Then the result should contain <result>

   Examples:
   | keyword | result |
   | "Listen" | "Silent" |
   | "Brag" | "Grab" |
   | "Cat" | "Act" |
   | "Fx" | "No Results" |

   Scenario Outline: Finding anagramatic words within a string
      Given the server is available
      When I provide <input> as input
      Then the result should contain <result>

   Examples:
   | input | result |
   | "listen to me"| "moisten" |
   | "Brett Noneman" | "bent" |
   | "Brett Noneman" | "meaner" |
   | "Demaree" | "dear" |
   | "fx" | "No results" |

   @other @wip
   Scenario: User submits a post to the service
      Given the server is available
      When the user submits a post
      Then the system returns an error code