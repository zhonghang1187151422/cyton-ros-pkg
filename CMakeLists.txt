cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

rosbuild_find_ros_package(actionlib_msgs)
include(${actionlib_msgs_PACKAGE_PATH}/cmake/actionbuild.cmake)
genaction()

rosbuild_init()

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#include_directories
#include_directories(${PROJECT_SOURCE_DIR}/include)

#link_directories
#link_directories(${PROJECT_SOURCE_DIR}/lib) 

#include_directories
include_directories($ENV{CYTON_INC})

#link_directories
link_directories($ENV{CYTON_LIB}) 

#uncomment if you have defined messages
rosbuild_genmsg()


rosbuild_add_executable(actinSE_node src/actinSE_node.cpp)
rosbuild_add_executable(guide_frame_node src/guide_frame_node.cpp)
rosbuild_add_executable(cyton_move_node src/cyton_move.cpp)
rosbuild_add_executable(set_home src/set_home.cpp)
rosbuild_add_executable(hardware_node src/hardware_node.cpp)
rosbuild_add_executable(send_joints src/send_joints.cpp)

target_link_libraries(actinSE_node  ecFoundCore ecActinSE ecCytonHardwareInterface) 
target_link_libraries(guide_frame_node ecFoundCore ecActinSE)
target_link_libraries(cyton_move_node ecFoundCore ecActinSE ecCytonHardwareInterface) 
target_link_libraries(set_home)
target_link_libraries(hardware_node ecFoundCore ecActinSE ecCytonHardwareInterface)
target_link_libraries(send_joints ecFoundCore ecActinSE ecCytonHardwareInterface)

