import trace
import sys

tracer = trace.Trace(trace=True, count=False)
tracer.run('exec(open("F:/RVC and stuff/apif/Retrieval-based-Voice-Conversion/rvc/api.py").read())')
