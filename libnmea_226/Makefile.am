SUBDIRS = src samples
#CC = gcc 

#BIN = lib/libnmea.a 
#SAMPLES = generate generator parse parse_file math

#MODULES = generate generator parse parser tok context time info gmath sentence  

 
#OBJ = $(MODULES:%=build/nmea_gcc/%.o) 
#LINKOBJ = $(OBJ) $(RES)

#SMPLS = $(SAMPLES:%=samples_%)
#SMPLOBJ = $(SAMPLES:%=samples/%/main.o)

ACLOCAL_AMFLAGS = -I m4

#INCS = -I include 
AM_CFLAGS = -I$(abs_srcdir)/src/nmea


#LIBS = -lm -Llib -lnmea
AM_LDFLAGS = -lm


EXTRA_DIST	= doc
							
					
# doxygen included in top level directory						
dox:
	doxygen	doc/nmea.doxygen
 
#.PHONY: all all-before all-after clean clean-custom doc
 
#all: all-before $(BIN) samples all-after 
#
#all-before:
#	mkdir -p build/nmea_gcc

#clean: clean-custom 
#	rm -f $(LINKOBJ) $(BIN) $(SMPLOBJ) $(SMPLS)

#doc:
#	$(MAKE) -C doc
	
#remake: clean all

#$(BIN): $(LINKOBJ)
#	ar rsc $@ $^
#	ranlib $@

#build/nmea_gcc/%.o: src/%.c 
#	$(CC) $(INCS) -c $< -o $@

#samples: $(SMPLS)

#samples_%: samples/%/main.o
#	$(CC) $< $(LIBS) -o build/$@

#samples/%/main.o: samples/%/main.c
#	$(CC) $(INCS) -c $< -o $@
