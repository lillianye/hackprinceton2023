#!/usr/bin/env python

#-----------------------------------------------------------------------
# runhack.py
# Author: Lillian Ye, Jessica Dong, Michelle Liu
#-----------------------------------------------------------------------

import sys
import securefile

def main():

    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + ' port', file = sys.stderr)
        sys.exit(1)

    try:
        port = int(sys.argv[1])
    except Exception:
        print('Port must be an integer.', file=sys.stderr)
        sys.exit(1)

    try:
        # print("running colo")
        securefile.app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
