# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.cmtk.convert import CFFConverter
def test_CFFConverter_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    publisher=dict(),
    gifti_labels=dict(),
    timeseries_files=dict(),
    description=dict(usedefault=True,
    ),
    gpickled_networks=dict(),
    creator=dict(),
    title=dict(),
    tract_files=dict(),
    script_files=dict(),
    graphml_networks=dict(),
    email=dict(),
    references=dict(),
    rights=dict(),
    gifti_surfaces=dict(),
    license=dict(),
    data_files=dict(),
    nifti_volumes=dict(),
    species=dict(usedefault=True,
    ),
    relation=dict(),
    out_file=dict(usedefault=True,
    ),
    )
    inputs = CFFConverter.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_CFFConverter_outputs():
    output_map = dict(connectome_file=dict(),
    )
    outputs = CFFConverter.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value