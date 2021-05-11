_base_ = [
    '../_base_/models/psanet_r50-d8.py', '../_base_/datasets/l430sv.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_20k.py'
]
model = dict(
    backbone=dict(frozen_stages=3),     #固定层的参数
    decode_head=dict(num_classes=11), auxiliary_head=dict(num_classes=11))

