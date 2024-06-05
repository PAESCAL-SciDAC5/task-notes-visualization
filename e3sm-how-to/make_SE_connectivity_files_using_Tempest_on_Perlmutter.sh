#!/bin/bash
#
################################################################################
# Script for generate connectivity files for HOMME's cubed sphere grids
# using Tempest on Perlmutter@NERSC. The connectivity files can be used,
# for example, to visualize EAM output with ParaView.
#
# Usage:
#
# <name-of-this-script> NE [PG]
#
# Examples:
# ------------------------------------------
#  grid    | command 
# ------------------------------------------
#  ne30pg2 | <name-of-this-script> 30
#  ne30pg4 | <name-of-this-script> 30 4
#  ne4pg2  | <name-of-this-script> 4
# ------------------------------------------
# 
# This script was only slightly modified from Mark Taylor's script at
# https://github.com/mt5555/remap-ncl/blob/master/makeSE.sh
#
################################################################################

#------------------------------------------------------------------
# Load the E3SM Unified environment to use Tempest
#------------------------------------------------------------------
source /global/common/software/e3sm/anaconda_envs/load_latest_e3sm_unified_pm-cpu.sh

#------------------------------------------------------------------
#  make SE template files
#------------------------------------------------------------------
wdir=~/mapping/grids

args=("$@")
if [ "$#" -lt "1" ]; then
    echo "Usage: <name-of-this-script> NE [PG]"
    exit 1
fi
PG=2
if [ "$#" -ge "2" ]; then
    PG=$2
fi

mkdir -p $wdir
cd $wdir

NE=$1
atmname=ne${NE}
atmgrid=TEMPEST_${atmname}.g
atm_pg=TEMPEST_${atmname}pg${PG}.g
atm_scrip=TEMPEST_${atmname}pg${PG}.scrip.nc

if [ -f $atm_scrip ] ; then
    echo reusing $atm_scrip
    exit 0
fi


# generate a Tempest NE8 mesh.  should match HOMME
GenerateCSMesh --alt --res $NE  --file $atmgrid
if [ "$PG" -ge 2 ]; then
    GenerateVolumetricMesh --in $atmgrid --out $atm_pg --np $PG --uniform
    ConvertMeshToSCRIP --in $atm_pg --out $atm_scrip
else
    # PG1 case is just the .g grid
    ConvertMeshToSCRIP --in $atmgrid --out $atm_scrip    
fi

echo
echo Output file in SCRIP format is ${wdir}/${atm_scrip}
echo
