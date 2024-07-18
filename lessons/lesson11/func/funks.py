from mylog import logging
def fibo(n):
    if n < 1:
        logging.info(f"fibo end")
        return 1
    else:
        logging.info(f"{n}")
        return fibo(n-1)+ fibo(n-2)