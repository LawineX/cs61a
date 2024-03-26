(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
(
car (cdr s)


)
)

(define (caddr s) 
(
car  (cddr s)


)
)

(define (sign val) 
(
cond
((< val 0) -1)
((=  val 0) 0)
((> val 0) 1)
)
)

(define (square x) (* x x))

(define (pow base exp) 
(
cond
((= 1 exp) base )
( (= 1 base ) 1 )
((even? exp)  (pow (square base)  (/ exp 2 ) ) )

( (odd? exp)  ( *  base   (pow (square base)  (/ (- exp 1)  2 ) ) ) )

)
)
