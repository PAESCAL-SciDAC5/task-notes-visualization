#!/bin/bash
#
################################################################################
# Script for generate connectivity files for HOMME's cubed sphere grids
# using Tempest on Compy.
# 
# Middle section ("make SE template files") slightly adapted from Mark Taylor's 
# script at https://github.com/mt5555/remap-ncl/blob/master/makeSE.sh
#
# First section (load environment) and last section (rename variables)
# added by Hui Wan, 2022-11.
################################################################################

#------------------------------------------------------------------
# Load the E3SM Unified environment to use Tempest
#------------------------------------------------------------------
source /share/apps/E3SM/conda_envs/load_latest_e3sm_unified_compy.sh

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

#------------------------------------------------------------------
# Create a copy of TEMPEST_${atmname}pg${PG}.scrip.nc
#               -> TEMPEST_${atmname}pg${PG}.scrip.renamed.nc
# with new dimension and variable names
#------------------------------------------------------------------
atm_scrip_renamed=${atm_scrip%.nc}.renamed.nc

ncrename -d grid_size,ncol  \
         -d grid_corners,ncorners \
         -v grid_center_lat,cell_center_lat \
         -v grid_center_lon,cell_center_lon \
         -v grid_corner_lat,cell_corner_lat \
         -v grid_corner_lon,cell_corner_lon \
         ${atm_scrip} \
         ${atm_scrip_renamed}

echo
echo Output file in SCRIP format with renamed variables and dimensions is ${wdir}/${atm_scrip_renamed}
echo


