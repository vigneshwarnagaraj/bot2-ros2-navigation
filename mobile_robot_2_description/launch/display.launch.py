import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('mobile_robot_2_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'Mobile.xacro')
    rviz_config = os.path.join(pkg_path, 'launch', 'display.rviz')
    robot_description = xacro.process_file(xacro_file).toxml()

    #robot State publisher -rsp
    rsp = Node(
        package = 'robot_state_publisher',
        executable = 'robot_state_publisher',
        output = 'screen',
        parameters = [{'robot_description': robot_description}],
    )

    #joint State publisher -jsp
    jsp_gui = Node(
        package = 'joint_state_publisher_gui',
        executable = 'joint_state_publisher_gui',
        output = 'screen',
    )

    #
    rviz = Node(
        package = 'rviz2',
        executable = 'rviz2',
        output = 'screen',
        arguments = ['-d', rviz_config],
    )

    return LaunchDescription([rsp, jsp_gui, rviz])
