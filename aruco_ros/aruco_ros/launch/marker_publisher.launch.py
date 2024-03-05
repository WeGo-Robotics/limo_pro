from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.utilities import perform_substitutions
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    aruco_marker_publisher_params = {
        'image_is_rectified': True,
        'marker_size': LaunchConfiguration('marker_size'),
        'reference_frame': LaunchConfiguration('reference_frame'),
        'camera_frame': 'camera_color_optical_frame',
    }

    aruco_marker_publisher = Node(
        package='aruco_ros',
        executable='marker_publisher',
        parameters=[aruco_marker_publisher_params],
        remappings=[('/camera_info', '/camera/color/camera_info'),
                    ('/image', '/camera/color/image_raw')],
    )

    return [aruco_marker_publisher]


def generate_launch_description():

    marker_size_arg = DeclareLaunchArgument(
        'marker_size', default_value='0.06',
        description='Marker size in m. '
    )

    reference_frame = DeclareLaunchArgument(
        'reference_frame', default_value='base_link',
        description='Reference frame.'
        'Leave it empty and the pose will be published wrt param parent_name. '
    )

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(marker_size_arg)
    ld.add_action(reference_frame)
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
