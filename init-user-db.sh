#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.signatures (
    patient_id VARCHAR(50) PRIMARY KEY,
    mhci DECIMAL,
    mhcii DECIMAL,
    coactivation_molecules DECIMAL,
    effector_cells DECIMAL,
    t_cell_traffic DECIMAL,
    nk_cells DECIMAL,
    t_cells DECIMAL,
    b_cells DECIMAL,
    m1_signatures DECIMAL,
    th1_signature DECIMAL,
    antitumor_cytokines DECIMAL,
    checkpoint_inhibition DECIMAL,
    treg DECIMAL,
    t_reg_traffic DECIMAL,
    neutrophil_signature DECIMAL,
    granulocyte_traffic DECIMAL,
    mdsc DECIMAL,
    mdsc_traffic DECIMAL,
    macrophages DECIMAL,
    macrophage_dc_traffic DECIMAL,
    th2_signature DECIMAL,
    protumor_cytokines DECIMAL,
    caf DECIMAL,
    matrix DECIMAL,
    matrix_remodeling DECIMAL,
    angiogenesis DECIMAL,
    endothelium DECIMAL,
    proliferation_rate DECIMAL,
    emt_signature DECIMAL
);
COPY content.signatures(
    patient_id,MHCI,MHCII,Coactivation_molecules,Effector_cells,T_cell_traffic,NK_cells,T_cells,B_cells,M1_signatures,Th1_signature,Antitumor_cytokines,Checkpoint_inhibition,Treg,T_reg_traffic,Neutrophil_signature,Granulocyte_traffic,MDSC,MDSC_traffic,Macrophages,Macrophage_DC_traffic,Th2_signature,Protumor_cytokines,CAF,Matrix,Matrix_remodeling,Angiogenesis,Endothelium,Proliferation_rate,EMT_signature
)
FROM '/app/signatures.csv'
DELIMITER ','
CSV HEADER;

EOSQL