# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/ams_ws/src/rf2o_laser_odometry

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/ams_ws/build/rf2o_laser_odometry

# Include any dependencies generated for this target.
include CMakeFiles/rf2o_laser_odometry.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/rf2o_laser_odometry.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/rf2o_laser_odometry.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/rf2o_laser_odometry.dir/flags.make

CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o: CMakeFiles/rf2o_laser_odometry.dir/flags.make
CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o: /home/pi/ams_ws/src/rf2o_laser_odometry/src/CLaserOdometry2D.cpp
CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o: CMakeFiles/rf2o_laser_odometry.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/ams_ws/build/rf2o_laser_odometry/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o -MF CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o.d -o CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o -c /home/pi/ams_ws/src/rf2o_laser_odometry/src/CLaserOdometry2D.cpp

CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/ams_ws/src/rf2o_laser_odometry/src/CLaserOdometry2D.cpp > CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.i

CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/ams_ws/src/rf2o_laser_odometry/src/CLaserOdometry2D.cpp -o CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.s

# Object files for target rf2o_laser_odometry
rf2o_laser_odometry_OBJECTS = \
"CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o"

# External object files for target rf2o_laser_odometry
rf2o_laser_odometry_EXTERNAL_OBJECTS =

librf2o_laser_odometry.a: CMakeFiles/rf2o_laser_odometry.dir/src/CLaserOdometry2D.cpp.o
librf2o_laser_odometry.a: CMakeFiles/rf2o_laser_odometry.dir/build.make
librf2o_laser_odometry.a: CMakeFiles/rf2o_laser_odometry.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/ams_ws/build/rf2o_laser_odometry/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library librf2o_laser_odometry.a"
	$(CMAKE_COMMAND) -P CMakeFiles/rf2o_laser_odometry.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rf2o_laser_odometry.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/rf2o_laser_odometry.dir/build: librf2o_laser_odometry.a
.PHONY : CMakeFiles/rf2o_laser_odometry.dir/build

CMakeFiles/rf2o_laser_odometry.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/rf2o_laser_odometry.dir/cmake_clean.cmake
.PHONY : CMakeFiles/rf2o_laser_odometry.dir/clean

CMakeFiles/rf2o_laser_odometry.dir/depend:
	cd /home/pi/ams_ws/build/rf2o_laser_odometry && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/ams_ws/src/rf2o_laser_odometry /home/pi/ams_ws/src/rf2o_laser_odometry /home/pi/ams_ws/build/rf2o_laser_odometry /home/pi/ams_ws/build/rf2o_laser_odometry /home/pi/ams_ws/build/rf2o_laser_odometry/CMakeFiles/rf2o_laser_odometry.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/rf2o_laser_odometry.dir/depend

