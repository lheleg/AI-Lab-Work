import contextlib
import sys
import time
from pyke import knowledge_engine, krb_traceback, goal
# Compile and load .krb files in same directory that I’m in (recursively).
engine = knowledge_engine.engine(__file__)

def testiraj_ekspertni_sistem():
    engine.reset() # Allows us to run tests multiple times.
    engine.activate('rules')
    start_time = time.time()
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    print("doing proof")
    try:
        with engine.prove_goal(
               'rules.treba_ponijeti($ponesi)') \
          as gen:
            for vars, plan in gen:
                if vars['ponesi'] == 'nista':
                    print ("\nNe trebate ponijeti ni kisobran ni kabanicu.")
                else: 
                    print ("\nTrebate ponijeti %s." % \
                    (vars['ponesi']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    
    try:
        with engine.prove_goal(
               'rules.treba_ponijeti_jos($ponesi)') \
          as gen:
            for vars, plan in gen:
                if vars['ponesi'] == 'nista':
                    print ("\nNe trebate ponijeti ni cizme ni masku.")
                else: 
                    print ("\nTrebate ponijeti %s." % \
                    (vars['ponesi']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    prove_time = time.time() - fc_end_time
    print()
    print("done")
