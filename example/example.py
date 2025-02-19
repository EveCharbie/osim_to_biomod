from osim_to_biomod import Converter, MuscleType, MuscleStateType

if __name__ == "__main__":
    model_path = "Models/"
    converter = Converter(
        model_path + "Wu_Shoulder_Model_via_points.bioMod",
        model_path + "Wu_Shoulder_Model_via_points.osim",
        ignore_muscle_applied_tag=False,
        ignore_fixed_dof_tag=False,
        ignore_clamped_dof_tag=False,
        mesh_dir="Geometry",
        muscle_type=MuscleType.HILL,
        state_type=MuscleStateType.DEGROOTE,
        print_warnings=True,
        print_general_informations=True,
        vtp_polygons_to_triangles=True,
    )
    converter.convert_file()
