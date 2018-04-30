from conans import ConanFile, MSBuild

class LmdbConan(ConanFile):
    name = "lmdb"
    version = "0.9.22"
    license = "MIT"
    url = "https://github.com/Ri0n/conan-lmdb"
    description = "Lightning Memory-Mapped Database from Symas"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone --depth 1 https://github.com/Ri0n/lmdb.git")

    def build(self):
        msbuild = MSBuild(self)
        #msbuild.TargetExt = [".lib",".dll"][self.options.shared == True]
        build_type = self.settings.get_safe("build_type")
        build_type += ["","DLL"][self.options.shared == True]
        msbuild.build("lmdb\\lmdb.sln", build_type=build_type)

    def package(self):
        self.copy("lmdb.h", dst="include", src="lmdb\\libraries\\liblmdb")
        self.copy("*lmdb*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        prefix = ["lib",""][self.options.shared == True]
        postfix = [" ","d"][self.settings.get_safe("build_type") == "Debug"]
        self.cpp_info.libs = [prefix + "lmdb" + postfix]

