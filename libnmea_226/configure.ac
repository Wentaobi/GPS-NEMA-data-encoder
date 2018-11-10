#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([libnmea], [0.5.31], [BUG-REPORT-ADDRESS])
AC_CONFIG_SRCDIR([src/context.c])
AC_CONFIG_HEADERS([config.h])

AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE()

# Checks for programs.
AC_PROG_CC
AC_PROG_CXX
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET


# new libtool initialize
LT_INIT

# Checks for libraries.
#AC_PROG_RANLIB

# Checks for header files.
AC_CHECK_HEADERS([float.h limits.h stdlib.h string.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_FUNC_MALLOC
AC_FUNC_MKTIME
AC_FUNC_STRTOD
AC_CHECK_FUNCS([memchr memset modf  strtol])

# FIXME: Replace `main' with a function in `-lm':
AC_CHECK_LIB([m], [cos])  
AC_CHECK_LIB([m], [pow])
AC_CHECK_LIB([m], [sqrt])

# OUTPUT SECTION
AC_CONFIG_FILES([Makefile])
AC_CONFIG_FILES([src/Makefile])
AC_CONFIG_FILES([samples/Makefile])
AC_CONFIG_FILES([samples/generate/Makefile])
AC_CONFIG_FILES([samples/generator/Makefile])
AC_CONFIG_FILES([samples/math/Makefile])
AC_CONFIG_FILES([samples/parse/Makefile])
AC_CONFIG_FILES([samples/parse_file/Makefile])



AC_OUTPUT
