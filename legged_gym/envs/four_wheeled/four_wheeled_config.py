from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO
import math

class FourWheeledCfg( LeggedRobotCfg ):
    class env( LeggedRobotCfg.env ):
        num_envs =  4096
        num_actions = 16
        num_observations = 60


    class terrain( LeggedRobotCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset( LeggedRobotCfg.asset ):
        file = "{LEGGED_GYM_ROOT_DIR}/resources/robots/four_wheeled/urdf/wheel_legged.urdf"
        name = "four_wheeled"
        foot_name = "wheel"
        terminate_after_contacts_on = ["base"]
        self_collisions = 1
        penalize_contacts_on = ["thigh", "calf"]
        flip_visual_attachments = False


    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.35] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            "LF_HAA": 0,
            "LH_HAA": 0,
            "RF_HAA": -0,
            "RH_HAA": -0,

            #"LF_HFE": -0.3154,
            #"LH_HFE": -0.3154,
            #"RF_HFE": -0.3154,
            #"RH_HFE": -0.3154,
            "LF_HFE": -0.,
            "LH_HFE": -0.,
            "RF_HFE": -0.,
            "RH_HFE": -0.,

            "LF_KFE": 0.5615,
            "LH_KFE": 0.5615,
            "RF_KFE": 0.5615,
            "RH_KFE": 0.5615,

            "LF_WHL": 0.0,
            "LH_WHL": 0.0,
            "RF_WHL": 0.0,
            "RH_WHL": 0.0,
        }

    class control( LeggedRobotCfg.control ):
        stiffness = {'HAA':40.,'HFE':60.,'KFE':60.,'WHL':40.}
        damping = {'HAA':2,'HFE':2,'KFE':2,'WHL':2}
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.5
        decimation = 4

    class rewards( LeggedRobotCfg.rewards ):
        only_positive_rewards = False
        base_height_target = 0.5
        max_contact_force = 500.
        class scales( LeggedRobotCfg.rewards.scales ):
            pass
        #   orientation = -5.0
        #    torques = -0.000025
        #   tracking_ang_vel = 1.0

class FourWheeledCfgPPO( LeggedRobotCfgPPO ):
        class runner( LeggedRobotCfgPPO.runner):
            run_name = ''
            experiment_name = 'flat_fourwheeled'



