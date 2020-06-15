package main

import (
	"sync"

	"github.com/sbinet/go-python"
)

func main() {
	// The following will also create the GIL explicitly
	// by calling PyEval_InitThreads(), without waiting
	// for the interpreter to do that
	python.Initialize()

	var wg sync.WaitGroup
	wg.Add(2)

	fooModule := python.PyImport_ImportModule("foo_goroutine")
	odds := fooModule.GetAttrString("print_odds")
	even := fooModule.GetAttrString("print_even")

	// Initialize() has locked the the GIL but at this point we don't need it
	// anymore. We save the current state and release the lock
	// so that goroutines can acquire it
	state := python.PyEval_SaveThread()

	go func() {
		_gstate := python.PyGILState_Ensure()
		odds.Call(python.PyTuple_New(0), python.PyDict_New())
		python.PyGILState_Release(_gstate)

		wg.Done()
	}()

	go func() {
		_gstate := python.PyGILState_Ensure()
		even.Call(python.PyTuple_New(0), python.PyDict_New())
		python.PyGILState_Release(_gstate)

		wg.Done()
	}()

	wg.Wait()

	// At this point we know we won't need Python anymore in this
	// program, we can restore the state and lock the GIL to perform
	// the final operations before exiting.
	python.PyEval_RestoreThread(state)
	python.Finalize()
}
