# Fresh Remedial Practice — Questions Only

**Suggested duration:** 50 minutes. **Total:** 50 marks. Written as new practice, not a transcription of the prior test.

**Instructions:** Show all main computational steps. Bisection: 4 decimals. Newton: 5 decimals. Do not open the answer key until you have attempted every part.

## A. Multiple-choice reasoning (10 marks; 2 marks each)

1. The true value is 80 and an estimate is 76. Which is the relative error? (A) 4 (B) 0.05 (C) 5 (D) 0.95
2. A polynomial is continuous with f(a)<0 and f(b)>0. Which method has a bracket-based convergence guarantee? (A) Newton (B) Secant (C) Bisection (D) Gradient descent
3. A central finite-difference estimate can worsen at extremely small h mainly due to: (A) measurement units (B) round-off cancellation (C) convexity (D) interpolation nodes
4. Which quantity is penalized by L2 regularization? (A) large coefficients (B) missing rows (C) negative labels (D) feature count directly
5. Composite Simpson's 1/3 rule with equal spacing requires the number of subintervals to be: (A) odd (B) prime (C) even (D) one

## B. Calculations and explanations (14 marks)

6. (4 marks) Actual values `[6,9,12]`, predictions `[5,10,11]`. Compute residuals and MSE, showing substitution.
7. (3 marks) Solve `3x + y = 10` and `x - y = 2`. Show elimination and verify both equations.
8. (4 marks) For `f(x)=x³`, estimate f'(1) using central difference with h=0.5. Explain why very small h may be harmful.
9. (3 marks) Given `(1,3)` and `(5,11)`, interpolate at x=2 and explain why extrapolating to x=6 is less reliable.

## C. Root-finding (18 marks)

Let `f(x)=x³-x-1`.

10. (9 marks) Check IVT on `[1,2]` (3 marks) and perform three bisection iterations in a table (6 marks). Report the third midpoint and final bracket.
11. (6 marks) Derive the Newton update (2 marks) and perform two Newton iterations starting from x0=1.5 (4 marks).
12. (3 marks) Explain why bisection and Newton may differ after equal numbers of steps, plus one advantage of each.

## D. Optimization (8 marks)

Let `J(w)=(w-5)²`, subject to `1≤w≤3`.

13. (2 marks) Identify variable, objective and constraint.
14. (2 marks) Find unconstrained and constrained minimizers.
15. (2 marks) Explain the difference and check the constrained objective value.
16. (2 marks) Determine convexity using derivatives and justify.

**After attempting:** check `solutions/remedial-mock-answers.md`, record errors in `progress/REVISION_LOG.md`, and redo missed questions without the key.
