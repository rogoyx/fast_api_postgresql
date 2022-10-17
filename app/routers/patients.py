from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from sql_app.database import get_db
from sql_app.models import signatures

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse(
        "welcome.html",
        {"request": request}
    )

@router.get("/patients_template/{patient_id}", response_class=HTMLResponse)
def read_id(
    request: Request,
    patient_id: str,
    db: Session = Depends(get_db)
):
    q_result = db.query(
        signatures.c.mhci,
        signatures.c.mhcii,
        signatures.c.coactivation_molecules,
        signatures.c.effector_cells,
        signatures.c.t_cell_traffic,
        signatures.c.nk_cells,
        signatures.c.t_cells,
        signatures.c.b_cells,
        signatures.c.m1_signatures,
        signatures.c.th1_signature,
        signatures.c.antitumor_cytokines,
        signatures.c.checkpoint_inhibition,
        signatures.c.treg,
        signatures.c.t_reg_traffic,
        signatures.c.neutrophil_signature,
        signatures.c.granulocyte_traffic,
        signatures.c.mdsc,
        signatures.c.mdsc_traffic,
        signatures.c.macrophages,
        signatures.c.macrophage_dc_traffic,
        signatures.c.th2_signature,
        signatures.c.protumor_cytokines,
        signatures.c.caf,
        signatures.c.matrix,
        signatures.c.matrix_remodeling,
        signatures.c.angiogenesis,
        signatures.c.endothelium,
        signatures.c.proliferation_rate,
        signatures.c.emt_signature
    ).filter(
        signatures.c.patient_id == patient_id
    )
    try:
        result = q_result.first()
        return templates.TemplateResponse(
            "patients.html",
            {"request": request,
                "patient_id": patient_id,
                "mhci": result["mhci"],
                "mhcii": result["mhcii"],
                "coactivation_molecules": result["coactivation_molecules"],
                "effector_cells": result["effector_cells"],
                "t_cell_traffic": result["t_cell_traffic"],
                "nk_cells": result["nk_cells"],
                "t_cells": result["t_cells"],
                "b_cells": result["b_cells"],
                "m1_signatures": result["m1_signatures"],
                "th1_signature": result["th1_signature"],
                "antitumor_cytokines": result["antitumor_cytokines"],
                "checkpoint_inhibition": result["checkpoint_inhibition"],
                "treg": result["treg"],
                "t_reg_traffic": result["t_reg_traffic"],
                "neutrophil_signature": result["neutrophil_signature"],
                "granulocyte_traffic": result["granulocyte_traffic"],
                "mdsc": result["mdsc"],
                "mdsc_traffic": result["mdsc_traffic"],
                "macrophages": result["macrophages"],
                "macrophage_dc_traffic": result["macrophage_dc_traffic"],
                "th2_signature": result["th2_signature"],
                "protumor_cytokines": result["protumor_cytokines"],
                "caf": result["caf"],
                "matrix": result["matrix"],
                "matrix_remodeling": result["matrix_remodeling"],
                "angiogenesis": result["angiogenesis"],
                "endothelium": result["endothelium"],
                "proliferation_rate": result["proliferation_rate"],
                "emt_signature": result["emt_signature"]
            }
        )
    except:
        return templates.TemplateResponse(
            "error.html",
            {"request": request,
             "patient_id": patient_id
            }
        )
        