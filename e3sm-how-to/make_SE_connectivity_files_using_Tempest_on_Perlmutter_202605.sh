#!/bin/bash
#
#  make SE template files given "NE" or a Exodus .g file
#
##########################################################
## Note:
##  This script is based on Mark Taylor's script at
##    https://github.com/mt5555/remap-ncl/blob/e29ce2c28b198cfcd8776a65b778284efb0f1348/makeSE.sh
##  The only changes are:
##    - Load the E3SM Unified environment for access to TempestRemap;
##      comment out "exit 1" in the first if-block
##    - Set $wdir to a personal path. 
##
##  Examples of usage
##    - To create an Exodus (.g) file and a SCRIP file for ne30pg2, use
##        ./${this_script} 30
##    - To create a SCRIP file for the NARRM (North America RRM) grid, use
##        ./${this_script} /global/cfs/cdirs/e3sm/inputdata/atm/cam/inic/homme/northamericax4v1.g
##########################################################
#
source /global/common/software/e3sm/anaconda_envs/load_latest_e3sm_unified_pm-cpu.sh

exepath=~/codes/tempestremap/
if ! [ -x $exepath/GenerateCSMesh ]; then
   # might be in our path, via conda:
   exepath=`which GenerateCSMesh`
   exepath=`dirname $exepath`
   echo $exepath
  #echo add some error checking if using this option
  #exit 1
fi

wdir=/global/cfs/projectdirs/m4359/huiwan/vis/connectivity/


args=("$@")
if [ "$#" -lt "1" ]; then
    echo "makeSE.sh NE or file.g [PG]"
    exit 1
fi
PG=2
if [ "$#" -ge "2" ]; then
    PG=$2
fi

set -x # turn on echo

cd $wdir
if [[ $1 == *".g"* ]]; then
    atmname=`basename $1 .g`
    echo $atmname
    atmgrid=$1
    atm_pg=${atmname}pg${PG}.g
    atm_scrip=${atmname}pg${PG}.scrip.nc
else
   NE=$1
   atmname=ne${NE}
   atmgrid=TEMPEST_${atmname}.g
   atm_pg=TEMPEST_${atmname}pg${PG}.g
   atm_scrip=TEMPEST_${atmname}pg${PG}.scrip.nc

   # generate a Tempest NE8 mesh.  should match HOMME
   $exepath/GenerateCSMesh --alt --res $NE  --file $atmgrid
fi


if [ -f $atm_scrip ] ; then
    echo reusing $atm_scrip
    exit 0
fi


if [ "$PG" -ge 2 ]; then
    $exepath/GenerateVolumetricMesh --in $atmgrid --out $atm_pg --np $PG --uniform
    $exepath/ConvertMeshToSCRIP --in $atm_pg --out $atm_scrip
else
    # PG1 case is just the .g grid
    $exepath/ConvertMeshToSCRIP --in $atmgrid --out $atm_scrip    
fi
