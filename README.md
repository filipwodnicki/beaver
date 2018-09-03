# About Woodcutting Algorithm

Woodcut Algorithm is a simple app built by Filip Wodnicki.  

## Project Description  

The app visualizes a solution to the <a href="https://en.wikipedia.org/wiki/Cutting_stock_problem">Cutting Stock Problem</a>, which describes how to optimally use material in a production process.  

The Algorithms are implemented via the Package [custo](https://github.com/filipwodnicki/custo).  

* <a href="https://github.com/bananalytics/beaver">Github repo</a>  
* <a href="https://woodcut-algorithm.herokuapp.com/about">Live app</a>  

The app runs on Python 3.6 and <a href="http://flask.pocoo.org">Flask</a>, a simple Python web framework. Miguel Grinberg's clear, concise and generally excellent <a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">Flask Mega Tutorial</a> provided inspiration to build this simple web app. It is hosted with Heroku.
  
---
  

## Algorithm description
 The tool takes Board Size and an Item List as inputs. It returns the optimal placement of items on a board, for production optimization.  

### Fit-first Algorithm
This app uses a Fit-First Algorithm, which a type of greedy approximation algorithm. It's called <a href="https://en.wikipedia.org/wiki/Greedy_algorithm">"greedy"</a> because it optimizes at each step without considering the solution and it's even as a greedy algorithm only an approximation of the optimal result, because it uses a short cut.  

Here's how it works:  

1. Sorts input pieces by size  
2. Creates the first Board which will be output  
3. Tries to arrange the largest item on the Board  
4. If there is space, the item is placed.  
5. If there is no space, a new Board is taken off the shelf and the item is added there.  
6. Repeat #3-5 for each item. Returns solution. Done.  

Interestingly, Fit-first has been shown to always give results within 20-25% of the truly optimal solution.  
  
---
  
  
## Changelog

* __Sep 3, 2018__
v0.3 Refactored to import Cutting Stock Problem Algorithms from [custo](https://github.com/filipwodnicki/custo)

* __Aug 25, 2018__  
v0.2 Implemented visualization using Chart.js  

* __Aug 6, 2018__  
v0.1 App is live! Implemented simple greedy algorithm.  

* __July 31, 2018__  
First github commit. Project started.  
