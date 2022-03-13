cd /app/project
rm -rf /app/project/data/train
rm -rf /app/project/data/val
rm -rf /app/project/data/test
python3 create_splits.py --source /app/project/data/waymo/training_and_validation/ --destination /app/project/data/
echo " Training count"
ls data/train | wc -l
echo " Val count"
ls data/val | wc -l
echo " Test count"
ls data/test | wc -l
echo " Training Files"
ls data/train
echo " Test Files"
ls data/test
echo " Validation Files"
ls data/val
