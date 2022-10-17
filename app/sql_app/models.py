from sqlalchemy import Column, Float, MetaData, String, Table

metadata_obj = MetaData()

signatures = Table(
    'signatures',
    metadata_obj,
    Column('patient_id', String, primary_key=True, index=True),
    Column('mhci', Float),
    Column('mhcii', Float),
    Column('coactivation_molecules', Float),
    Column('effector_cells', Float),
    Column('t_cell_traffic', Float),
    Column('nk_cells', Float),
    Column('t_cells', Float),
    Column('b_cells', Float),
    Column('m1_signatures', Float),
    Column('th1_signature', Float),
    Column('antitumor_cytokines', Float),
    Column('checkpoint_inhibition', Float),
    Column('treg', Float),
    Column('t_reg_traffic', Float),
    Column('neutrophil_signature', Float),
    Column('granulocyte_traffic', Float),
    Column('mdsc', Float),
    Column('mdsc_traffic', Float),
    Column('macrophages', Float),
    Column('macrophage_dc_traffic', Float),
    Column('th2_signature', Float),
    Column('protumor_cytokines', Float),
    Column('caf', Float),
    Column('matrix', Float),
    Column('matrix_remodeling', Float),
    Column('angiogenesis', Float),
    Column('endothelium', Float),
    Column('proliferation_rate', Float),
    Column('emt_signature', Float),
    schema='content'
)