## You need to run:
```
go get github.com/sbinet/go-python

export PYHTONPATH={PATH_WHERE_YOUR_PYC_FILES_LOCATED}

go build main.go &&  ./main
```

The last line will create a pyc files for you
<hr>

## Troubleshooting:
If you encounter this:
```
github.com/sbinet/go-python
# pkg-config --cflags  -- python-2.7
Package python-2.7 was not found in the pkg-config search path.
Perhaps you should add the directory containing `python-2.7.pc'
to the PKG_CONFIG_PATH environment variable
No package 'python-2.7' found
pkg-config: exit status 1
```

Run this:
```
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/System/Library/Frameworks/Python.framework/Versions/2.7/lib/pkgconfig
```