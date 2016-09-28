def thing():
    print("starting")
    print("blah blah blah")
    print("yielding 1")
    yield 1
# -------------------- CUT HERE --------------------
    print("running")
    print("blah blah blah")
    print("yielding 2")
    yield 2
# -------------------- CUT HERE --------------------
    print("done")


t = Thing()                          # run nothing at all
print("got from next(t):", next(t))  # run the first piece
print("got from next(t):", next(t))  # run the second piece
print("got from next(t):", next(t))  # run the last piece and raise StopIteration
