# Python Arbitrary Argument Lists
# Any formal parameters which occur after the *args parameter are ‘keyword-only’ 
# arguments, meaning that they can only be used as keywords rather than positional arguments.

    def concat(*args, sep="/"):
        return sep.join(args)

    concat("earth", "mars", "venus")
    concat("earth", "mars", "venus", sep=".")
