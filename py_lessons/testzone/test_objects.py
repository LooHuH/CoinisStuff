def use(function: object, *args):
    function(args)
    
def test(args):
    print(' '.join(x for x in args))
    
use(test, 'this is', 'a test')