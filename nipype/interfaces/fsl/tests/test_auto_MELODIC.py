# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.model import MELODIC
def test_MELODIC_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    dim_est=dict(argstr='--dimest=%s',
    ),
    out_dir=dict(argstr='-o %s',
    genfile=True,
    ),
    pbsc=dict(argstr='--pbsc',
    ),
    smode=dict(argstr='--smode=%s',
    ),
    out_orig=dict(argstr='--Oorig',
    ),
    sep_whiten=dict(argstr='--sep_whiten',
    ),
    t_des=dict(argstr='--Tdes=%s',
    ),
    maxit=dict(argstr='--maxit=%d',
    ),
    report_maps=dict(argstr='--report_maps=%s',
    ),
    t_con=dict(argstr='--Tcon=%s',
    ),
    num_ICs=dict(argstr='-n %d',
    ),
    no_mm=dict(argstr='--no_mm',
    ),
    log_power=dict(argstr='--logPower',
    ),
    var_norm=dict(argstr='--vn',
    ),
    cov_weight=dict(argstr='--covarweight=%f',
    ),
    tr_sec=dict(argstr='--tr=%f',
    ),
    mix=dict(argstr='--mix=%s',
    ),
    out_all=dict(argstr='--Oall',
    ),
    epsilonS=dict(argstr='--epsS=%f',
    ),
    approach=dict(argstr='-a %s',
    ),
    update_mask=dict(argstr='--update_mask',
    ),
    no_mask=dict(argstr='--nomask',
    ),
    out_mean=dict(argstr='--Omean',
    ),
    bg_threshold=dict(argstr='--bgthreshold=%f',
    ),
    out_unmix=dict(argstr='--Ounmix',
    ),
    sep_vn=dict(argstr='--sep_vn',
    ),
    epsilon=dict(argstr='--eps=%f',
    ),
    args=dict(argstr='%s',
    ),
    rem_cmp=dict(argstr='-f %d',
    ),
    remove_deriv=dict(argstr='--remove_deriv',
    ),
    bg_image=dict(argstr='--bgimage=%s',
    ),
    non_linearity=dict(argstr='--nl=%s',
    ),
    out_pca=dict(argstr='--Opca',
    ),
    output_type=dict(),
    report=dict(argstr='--report',
    ),
    s_con=dict(argstr='--Scon=%s',
    ),
    dim=dict(argstr='-d %d',
    ),
    s_des=dict(argstr='--Sdes=%s',
    ),
    no_bet=dict(argstr='--nobet',
    ),
    mask=dict(argstr='-m %s',
    ),
    in_files=dict(argstr='-i %s',
    mandatory=True,
    position=0,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    max_restart=dict(argstr='--maxrestart=%d',
    ),
    mm_thresh=dict(argstr='--mmthresh=%f',
    ),
    ICs=dict(argstr='--ICs=%s',
    ),
    out_stats=dict(argstr='--Ostats',
    ),
    out_white=dict(argstr='--Owhite',
    ),
    )
    inputs = MELODIC.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_MELODIC_outputs():
    output_map = dict(report_dir=dict(),
    out_dir=dict(),
    )
    outputs = MELODIC.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
