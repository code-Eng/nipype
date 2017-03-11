# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..longitudinal import FuseSegmentations


def test_FuseSegmentations_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_norms=dict(argstr='-n %s',
    mandatory=True,
    ),
    in_segmentations=dict(argstr='-a %s',
    mandatory=True,
    ),
    in_segmentations_noCC=dict(argstr='-c %s',
    mandatory=True,
    ),
    out_file=dict(mandatory=True,
    position=-1,
    ),
    subject_id=dict(argstr='%s',
    position=-3,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    timepoints=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    )
    inputs = FuseSegmentations.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FuseSegmentations_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = FuseSegmentations.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value