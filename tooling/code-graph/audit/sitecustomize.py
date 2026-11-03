import sys, os, json
_L=os.environ.get('CODE_GRAPH_AUDIT')
if _L:
    _f=open(_L,'a',buffering=1)
    _W=('socket.','urllib.','subprocess.','os.system','os.exec','os.posix_spawn','http.client.')
    def _h(ev,args):
        if ev.startswith(_W):
            try: _f.write(json.dumps([os.getpid(),ev,repr(args)[:300]])+'\n')
            except Exception: pass
    sys.addaudithook(_h)
