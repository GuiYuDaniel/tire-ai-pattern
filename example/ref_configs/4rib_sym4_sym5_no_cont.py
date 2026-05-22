"""
参考配置 1.8：4个RIB，对称性4和5双候选，无连续性
方案: symmetry_4 或 symmetry_5
RIB数量: 4
对称性候选: [symmetry_4, symmetry_5]
连续性候选: 无
"""

from pathlib import Path
from src.models.enums import RegionEnum, DecorationPositionEnum
from src.utils.image_utils import load_image_to_base64

CONFIG = {
    "scheme_rank": 1,
    "is_debug": False,
    "big_image": None,
    "small_images": [
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib1.png"), with_prefix=True), "region": RegionEnum.SIDE},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib2.png"), with_prefix=True), "region": RegionEnum.CENTER},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib3.png"), with_prefix=True), "region": RegionEnum.CENTER},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib4.png"), with_prefix=True), "region": RegionEnum.SIDE},
    ],
    "rules_config": [
        {"rule": "rule1", "description": "rib无对称", "max_score": 10},
        {"rule": "rule2", "description": "rib中心对称", "max_score": 10},
        {"rule": "rule6", "description": "节距纵向关系无缝拼接", "max_score": 10},
        {
            "rule": "rule8",
            "description": "横沟数量约束",
            "max_score": 4,
            "groove_width_center": 25.0,
            "groove_width_side": 13.0,
        },
        {
            "rule": "rule11",
            "description": "纵向钢片与细沟数量约束",
            "max_score": 4,
            "groove_width": 1,
            "min_width_offset_px": 1,
            "edge_margin_ratio": 0.1,
            "min_segment_length_ratio": 0.5,
            "max_angle_from_vertical": 10,
            "max_count_center": 3,
            "max_count_side": 2,
        },
        {
            "rule": "rule13",
            "description": "海陆比28%-35%",
            "max_score": 2,
            "land_ratio_min": 0.28,
            "land_ratio_max": 0.35,
        },
        {
            "rule": "rule100", "rib_number": 4,
            "rib_sizes": [
                {"rib_name": "rib1", "num_pitchs": 5, "rib_width": 400, "rib_height": 640},
                {"rib_name": "rib2", "num_pitchs": 5, "rib_width": 200, "rib_height": 640},
                {"rib_name": "rib3", "num_pitchs": 5, "rib_width": 200, "rib_height": 640},
                {"rib_name": "rib4", "num_pitchs": 5, "rib_width": 400, "rib_height": 640},
            ],
        },
        {
            "rule": "rule101",
            "groove_sizes": [
                {"groove_width": 20, "groove_height": 640},
                {"groove_width": 20, "groove_height": 640},
                {"groove_width": 20, "groove_height": 640},
            ],
        },
        {
            "rule": "rule102",
            "decorations": [
                {"position": DecorationPositionEnum.LEFT, "decoration_width": 300, "decoration_height": 640, "decoration_opacity": 128},
            ],
        },
    ],
}

from src.config._builder import build_tire_struct

tire_struct = build_tire_struct(CONFIG)
