CXX = clang++ -mmacosx-version-min=14.6 -std=c++20
EXT_SUFFIX = .so
ifeq ($(PYTHON_HOME),)
CXXFLAGS = $(shell pkg-config --cflags python3)
LDFLAGS = $(shell pkg-config --libs python3)
else
CXXFLAGS = -I$(PYTHON_HOME)/include/python3.15d
LDFLAGS = -L$(PYTHON_HOME)/lib -lpython3.15d
endif


all: demo

generated_inittab_modules.h generated_inittab_entries.h: generate_inittab_headers.py
	python3 $< --num_extensions 10000

main.o: main.cpp generated_inittab_modules.h generated_inittab_entries.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

demo: main.o
	$(CXX) main.o $(LDFLAGS) -o demo

clean:
	rm -f *.o *.so *.dylib demo generated_inittab_modules.h generated_inittab_entries.h
