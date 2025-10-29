#!/bin/bash
# The interpreter used to execute the script 
#SBATCH --job-name=eecs542_hw4
#SBATCH --mail-user=aryamanr@umich.edu
#SBATCH --mail-type=BEGIN,END
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=32G
#SBATCH --time=01:00:00
#SBATCH --account=eecs542f25_class
#SBATCH --partition=gpu_mig40,gpu,spgpu       
#SBATCH --gres=gpu:1           
#SBATCH --output=eecs542_hw4_1.log
#SBATCH --error=eecs542_hw4_1.err

echo "hello world"
source /home/aryamanr/.bashrc
conda activate nerf


cd /scratch/eecs542f25_class_root/eecs542f25_class/aryamanr/hw4nvs
#python run_nerf.py --config configs/lego_coarse.txt
python run_nerf.py --config configs/lego_fine.txt