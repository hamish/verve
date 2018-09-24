Verve: Bring enthusiasm and vigor to miantianing your AWS infrastructure.


usage: verve command [options] 

verge generate -v version_label output_directory -d verve_project_directory
verve launch stack_name -p project_name -l version_label [-o parameter_name=value [-o parameter_name=value]
verve update_version stack_name -l version_label
verve launch_child_stack parent_stack_name -t template_name
verve delete_child_stack parent_stack_name -t template_name
verve apply_policy stack_name policy_name
verve remove_policy stack_name


