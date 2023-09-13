# CMPS 2200  Recitation 02

**Name (Team Member 1):** Rhon Farber  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**Asymptotic Behavior**
Using: a = 2, b = 2, for n = 10,20,100,100,1000,2000
Using: W(n) = O(nlog_b a)

1. f(n) = 1
The behavior is W(n) = O(n)
Evidence:
|     n |     n |
|-------|-------|
|    10 |    31 |
|    20 |    63 |
|   100 |   255 |
|  1000 |  2047 |
|  2000 |  4095 |
| 10000 | 32767 |

2. f(n) = log n
The behavior is W(n) = O(nlog(n))
Actual Values: for n = 10,20,100,100,1000,2000
Evidence:
|     n |   nlog n |
|-------|----------|
|    10 |    3.452 |
|    20 |    9.899 |
|   100 |  108.258 |
|  1000 | 1362.700 |
|  2000 | 2733.001 |
| 10000 | 6524.228 |

4. f(n) = n
The behavior is W(n) = O(n^2)
Actual Values: for n = 10,20,100,100,1000,2000
Evidence:
|     n |     n^2    |
|-------|------------|
|    10 |       50.0 |
|    20 |      120.0 |
|   100 |      800.0 |
|  1000 |    11000.0 |
|  2000 |    24000.0 |
| 10000 |   150000.0 |

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

1. if c < logb a then the algorithm takes less time to complete as the input size increases because the work function grows slower than the number of operations. The behavior is O(n^(logb a)) because the number of operations grows at O(n^log_b a) and the work function grows at O(n^c). (root dominated)
2. if c = logb a then the algorithm's work function and number of operations are growing at the same pace, so the behavior is O(n^c) = (n^log_b a). (balanced)
3. if c > logb a then the algorithm takes more time to complete as the input size increases because the work function grows quicker than the number of operations. The behavior is then O(n^c) because the number of operations grows at O(n^log_b a) and the work function grows at O(n^c). (leaf dominated)

Given the results:
[(10, 35.55235148617739, 88.88087871544349), (20, 75.57683892735437, 267.20447653087854), (50, 176.06601717798213, 1100.4126073623884), (100, 362.13203435596427, 3200.8252147247767), (1000, 3378.597071955948, 105581.15849862341), (5000, 21680.256121069153, 1197676.2594585277), (10000, 43460.512242138306, 3395352.5189170553)]
for n^0.5 which is c < logb a the values increase, but not as rapidly as for n^1.5 which is correct for the behavior.
for n^1.5 the values increase much more rapidly which is in line with the behavior as well.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
1. for f(n) = 1
The depth of the tree is logn, so the span is O(log n)
2. for f(n) = log n
The span should be O(log^2 n)
3. for f(n) = n
The span should be O(n * log n)
Given the results:
[(10, 341, 341), (20, 1365, 1365), (50, 5461, 5461), (100, 21845, 21845), (1000, 1398101, 1398101), (5000, 89478485, 89478485), (10000, 357913941, 357913941)]
Everything matches the spans.
