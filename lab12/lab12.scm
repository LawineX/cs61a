(define (tail-replicate x n)
  (define (helper now n)
    (cond((= n 0) now)
      (else (helper (cons x now) (- n 1)))

      )

    )
    (helper nil n)
  )

(define-macro (def func args body)

  `(define ,func (lambda ,args ,body))


  )

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x) ))
        (* y y y))))
