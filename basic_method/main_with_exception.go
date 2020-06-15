// main.go
package main

import (
	"fmt"

	"github.com/sbinet/go-python"
)

func main() {
	python.Initialize()
	defer python.Finalize()

	fooModule := python.PyImport_ImportModule("foo_with_exception")
	if fooModule == nil {
		panic("Error importing module")
	}

	helloFunc := fooModule.GetAttrString("hello")
	if helloFunc == nil {
		panic("Error importing function")
	}

	// The Python function takes no params but when using the C api
	// we're required to send (empty) *args and **kwargs anyways.
	var aaa = helloFunc.Call(python.PyTuple_New(0), python.PyDict_New())
	fmt.Println(aaa)
}
