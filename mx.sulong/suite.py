suite = {
  "mxversion" : "5.70.2",
  "name" : "sulong",
  "versionConflictResolution" : "latest",

  "imports" : {
    "suites" : [
      {
        "name" : "truffle",
        "subdir" : True,
        "version" : "343588a760902169386b0ef2a32756e3d64578a4",
        "urls" : [
          {"url" : "https://github.com/graalvm/graal", "kind" : "git"},
          {"url" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind" : "binary"},
        ]
      },
    ],
  },

  "javac.lint.overrides" : "none",

  "libraries" : {
    "LLVM_TEST_SUITE" : {
      "path" : "tests/test-suite-3.2.src.tar.gz",
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/sulong-deps/test-suite-3.2.src.tar.gz",
        "http://llvm.org/releases/3.2/test-suite-3.2.src.tar.gz",
      ],
      "sha1" : "e370255ca2540bcd66f316fe5b96f459382f3e8a",
    },
    "GCC_SOURCE" : {
      "path" : "tests/gcc-5.2.0.tar.gz",
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/sulong-deps/gcc-5.2.0.tar.gz",
        "http://gd.tuwien.ac.at/gnu/gcc/releases/gcc-5.2.0/gcc-5.2.0.tar.gz",
        "ftp://ftp.fu-berlin.de/unix/languages/gcc/releases/gcc-5.2.0/gcc-5.2.0.tar.gz",
        "http://mirrors-usa.go-parts.com/gcc/releases/gcc-5.2.0/gcc-5.2.0.tar.gz",
      ],
      "sha1" : "713211883406b3839bdba4a22e7111a0cff5d09b",
    },
    "SHOOTOUT_SUITE" : {
      "path" : "tests/benchmarksgame-scm-latest.tar.gz",
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/sulong-deps/benchmarksgame-scm-latest.tar.gz",
      ],
      "sha1" : "9684ca5aaa38ff078811f9b42f15ee65cdd259fc",
    },
    "NWCC_SUITE" : {
      "path" : "tests/nwcc_0.8.3.tar.gz",
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/sulong-deps/nwcc_0.8.3.tar.gz",
      ],
      "sha1" : "2ab1825dc1f8bd5258204bab19e8fafad93fef26",
    },
    "LTA_REF" : {
      "path" : "tests/lifetime-analysis-ref-3.tar.gz",
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/sulong-deps/lifetime-analysis-ref-3.tar.gz",
      ],
      "sha1" : "679f71fcf99674a0972b48740ca810dfc1ae2255",
    },
    "COCO" : {
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/sulong-deps/Coco.jar"
      ],
      "sha1" : "f204783009ab88838b5118adce58eca4368acd94",
    },
  },

  "projects" : {

    "com.oracle.truffle.llvm.test" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm",
        "com.oracle.truffle.llvm.pipe",
        "truffle:TRUFFLE_TCK",
        "mx:JUNIT",
      ],
      "checkstyle" : "com.oracle.truffle.llvm.test",
      "annotationProcessors" : ["SULONG_OPTIONS_PROCESSOR"],
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },
    "com.oracle.truffle.llvm.test.native" : {
      "subDir" : "projects",
      "native" : True,
      "vpath" : True,
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.types.test" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.runtime",
        "mx:JUNIT",
      ],
      "checkstyle" : "com.oracle.truffle.llvm.test",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.runtime" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.option",
        "truffle:TRUFFLE_API",
        "truffle:TRUFFLE_NFI",
      ],
      "checkstyle" : "com.oracle.truffle.llvm.runtime",
      "annotationProcessors" : ["SULONG_OPTIONS_PROCESSOR",
        "truffle:TRUFFLE_DSL_PROCESSOR"],
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },


    "com.oracle.truffle.llvm.nodes" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.runtime"
      ],
      "checkstyle" : "com.oracle.truffle.llvm.runtime",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.parser" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.runtime",
       ],
      "checkstyle" : "com.oracle.truffle.llvm",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.parser.factories",
       ],
      "checkstyle" : "com.oracle.truffle.llvm",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.asm.amd64.parser" : {
      "subDir" : "projects",
      "native" : True,
      "dependencies" : [
        "COCO"
      ],
      "buildEnv" : {
        "COCO_JAR" : "<path:COCO>",
      },
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.asm.amd64" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.nodes",
      ],
      "buildDependencies" : [
        "com.oracle.truffle.llvm.asm.amd64.parser",
      ],
      "checkstyle" : "com.oracle.truffle.llvm",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.parser.factories" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.asm.amd64",
        "com.oracle.truffle.llvm.parser",
       ],
      "checkstyle" : "com.oracle.truffle.llvm",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.pipe" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "javaProperties" : {
        "test.pipe.lib" : "<path:SULONG_TEST_NATIVE>/<lib:pipe>",
      },
      "checkstyle" : "com.oracle.truffle.llvm.test",
      "javaCompliance" : "1.8",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.pipe.native" : {
      "subDir" : "projects",
      "native" : True,
      "vpath" : True,
      "results" : [
        "bin/<lib:pipe>",
      ],
      "buildDependencies" : [
        "com.oracle.truffle.llvm.pipe",
      ],
      "buildEnv" : {
        "LIBPIPE" : "<lib:pipe>",
        "OS" : "<os>",
      },
      "checkstyle" : "com.oracle.truffle.llvm.test",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.option" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "checkstyle" : "com.oracle.truffle.llvm",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },

    "com.oracle.truffle.llvm.option.processor" : {
      "subDir" : "projects",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.llvm.option",
      ],
      "checkstyle" : "com.oracle.truffle.llvm",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle, LLVM",
      "license" : "BSD-new",
    },
    "com.oracle.truffle.llvm.libraries.bitcode" : {
      "subDir" : "projects",
      "native" : True,
      "vpath" : True,
      "results" : [
        "bin/libsulong.bc",
      ],
      "license" : "BSD-new",
    },
    "com.oracle.truffle.llvm.libraries.native" : {
      "subDir" : "projects",
      "native" : True,
      "vpath" : True,
      "results" : [
        "bin/<lib:sulong>",
      ],
      "buildEnv" : {
        "LIBSULONG" : "<lib:sulong>",
        "OS" : "<os>",
      },
      "license" : "BSD-new",
    },
  },

  "distributions" : {
    "SULONG" : {
      "path" : "build/sulong.jar",
      "subDir" : "graal",
      "sourcesPath" : "build/sulong.src.zip",
      "mainClass" : "com.oracle.truffle.llvm.LLVM",
      "dependencies" : ["com.oracle.truffle.llvm"],
      "distDependencies" : [
        "truffle:TRUFFLE_API",
        "truffle:TRUFFLE_NFI",
        "SULONG_OPTIONS",
      ],
      "license" : "BSD-new",
    },

    "SULONG_LIBS" : {
      "native" : True,
      "relpath" : False,
      "platformDependent" : True,
      "output" : "mxbuild/sulong-libs",
      "dependencies" : [
        "com.oracle.truffle.llvm.libraries.bitcode",
        "com.oracle.truffle.llvm.libraries.native",
      ],
      "license" : "BSD-new",
    },

    "SULONG_OPTIONS" : {
      "path" : "build/sulong_options.jar",
      "subDir" : "graal",
      "javaCompliance" : "1.8",
      "dependencies" : ["com.oracle.truffle.llvm.option"],
      "description" : "The Sulong Option interface.",
      "license" : "BSD-new",
    },
    "SULONG_OPTIONS_PROCESSOR" : {
      "path" : "build/sulong_options_processor.jar",
      "subDir" : "graal",
      "javaCompliance" : "1.8",
      "dependencies" : ["com.oracle.truffle.llvm.option.processor"],
      "distDependencies" : [
        "SULONG_OPTIONS",
      ],
      "description" : "The Sulong Option Processor generates an option class declared using options annotations.",
      "license" : "BSD-new",
    },

    "SULONG_TEST" : {
      "path" : "build/sulong_test.jar",
      "subDir" : "graal",
      "sourcesPath" : "build/sulong_test.src.zip",
      "dependencies" : [
        "com.oracle.truffle.llvm.test",
        "com.oracle.truffle.llvm.types.test",
        "com.oracle.truffle.llvm.pipe"
      ],
      "exclude" : [
       "mx:JUNIT"
      ],
      "distDependencies" : [
        "truffle:TRUFFLE_API",
        "truffle:TRUFFLE_TCK",
        "sulong:SULONG",
        "SULONG_TEST_NATIVE",
      ],
      "license" : "BSD-new",
    },

    "SULONG_TEST_NATIVE" : {
      "native" : True,
      "platformDependent" : True,
      "output" : "mxbuild/sulong-test-native",
      "dependencies" : [
        "com.oracle.truffle.llvm.pipe.native",
      ],
      "license" : "BSD-new",
    },
  }
}