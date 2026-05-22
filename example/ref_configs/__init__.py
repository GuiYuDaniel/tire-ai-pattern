"""Reference configs for pipeline1.

Each file is a standalone config module exporting CONFIG (dict) and tire_struct.
Because filenames start with digits, use importlib.import_module() to access them.
Import via the prefixed name, e.g.:
    from example.ref_configs import cfg_5rib_sym0_no_cont
    result = run_pipeline1(cfg_5rib_sym0_no_cont.tire_struct)

Users can also directly read the .py files in this directory as reference.
"""

import importlib as _importlib

_MODULES = [
    "5rib_sym0_no_cont",
    "5rib_sym1_no_cont",
    "5rib_sym2_no_cont",
    "5rib_sym0_cont1",
    "5rib_sym1_cont1",
    "5rib_sym2_cont2",
    "4rib_sym4_no_cont",
    "4rib_sym4_sym5_no_cont",
    "4rib_sym456_no_cont",
    "4rib_sym456_cont3",
    "4rib_sym456_cont123_bad",
]

for _name in _MODULES:
    _mod = _importlib.import_module(f"example.ref_configs.{_name}")
    globals()[f"cfg_{_name}"] = _mod
