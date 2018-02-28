objects = main.o context.o generator.o info.o \
	parse.o sentence.o tok.o generate.o \
   	 gmath.o parser.o time.o

wentao : $(objects)
	gcc -o wentao $(objects) -lm

main.o : nmea.h
	gcc -c main.c
context.o : context.h
	gcc -c context.c
info.o : info.h nmea_time.h
	gcc -c info.c
parse.o : tok.h parse.h context.h gmath.h units.h sentence.h config.h
	gcc -c parse.c
sentence.o : sentence.h info.h nmea_time.h
	gcc -c sentence.c
tok.o : tok.h config.h
	gcc -c tok.c
generate.o : tok.h sentence.h generate.h units.h config.h
	gcc -c generate.c
generator.o : gmath.h generate.h generator.h context.h info.h nmea_time.h
	gcc -c generator.c
gmath.o : gmath.h info.h nmea_time.h
	gcc -c gmath.c
parser.o : tok.h parse.h parser.h context.h config.h
	gcc -c parser.c
time.o : nmea_time.h
	gcc -c time.c

.PHONY : clean
clean :
	-rm wentao $(objects)
	-rm -f *.o
