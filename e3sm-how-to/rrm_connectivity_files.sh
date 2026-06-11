exodus_file_path=/global/cfs/cdirs/e3sm/inputdata/atm/cam/inic/homme/
for grid in amazonx4v1 antarcticax4v1 arcticx4v1 conusx4v1
#enax4v1 perux4v1 twpx4v1
#northamericax4v1
do
  ./make_SE_connectivity_files_using_Tempest_on_Perlmutter_202605.sh ${exodus_file_path}/${grid}.g
done
