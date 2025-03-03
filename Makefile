
PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin
DESTDIR ?=

# I like symlinks since it doesn't require reinstalling when it changes
.PHONY: install
install: uninstall
	mkdir -p $(DESTDIR)$(BINDIR)/
	ln -s $(shell pwd)/flash $(DESTDIR)$(BINDIR)/flash

.PHONY: uninstall
uninstall:
	unlink $(DESTDIR)$(BINDIR)/flash

