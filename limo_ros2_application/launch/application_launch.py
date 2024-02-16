from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    limo_ros2_application_dir = get_package_share_directory('limo_ros2_application')
    parameters_file_dir = os.path.join(limo_ros2_application_dir, 'params')
    parameters_file_path = os.path.join(parameters_file_dir, 'detect_line.yaml')
    os.environ['FILE_PATH'] = str(parameters_file_dir)
    return LaunchDescription([
        Node(
            package='limo_ros2_application',
            executable='detect_line',
            name='detect_line',
            parameters=[parameters_file_path]
        ),
        Node(
            package='limo_ros2_application',
            executable='limo_e_stop',
            name='limo_e_stop'
        ),
        Node(
            package='limo_ros2_application',
            executable='limo_control',
            name='limo_control'
        )
    ])