# Training Process
#export CUDA_VISIBLE_DEVICES=0
python experiments/model_main_tf2.py --model_dir=training/reference/ --pipeline_config_path=training/reference/pipeline_new.config &
# evaluation Process
#Start the evaluation process on CPU
#Edit File "/usr/local/lib/python3.8/dist-packages/numpy/core/function_base.py", line 121. Fix index integer issue.
export CUDA_VISIBLE_DEVICES=-1
python experiments/model_main_tf2.py --model_dir=training/reference/ --pipeline_config_path=training/reference/pipeline_new.config --checkpoint_dir=training/reference &

