from __future__ import annotations

from fastapi import APIRouter, Depends

from src.agent.runtime import Runtime
from src.api.v1.dependencies import get_runtime
from src.tools.check_visa_requirements import VisaRequirementsInput, VisaRequirementsOutput
from src.tools.estimate_budget import EstimateBudgetInput, EstimateBudgetOutput
from src.tools.get_points_of_interest import PointsOfInterestInput, PointsOfInterestOutput


router = APIRouter(prefix="/tools", tags=["v1"])


@router.post("/points_of_interest", response_model=PointsOfInterestOutput)
def points_of_interest(req: PointsOfInterestInput, rt: Runtime = Depends(get_runtime)) -> PointsOfInterestOutput:
    out = rt.orchestrator_v1.registry.dispatch("get_points_of_interest", req.model_dump())
    return PointsOfInterestOutput.model_validate(out)


@router.post("/visa_requirements", response_model=VisaRequirementsOutput)
def visa_requirements(req: VisaRequirementsInput, rt: Runtime = Depends(get_runtime)) -> VisaRequirementsOutput:
    out = rt.orchestrator_v1.registry.dispatch("check_visa_requirements", req.model_dump())
    return VisaRequirementsOutput.model_validate(out)


@router.post("/estimate_budget", response_model=EstimateBudgetOutput)
def budget(req: EstimateBudgetInput, rt: Runtime = Depends(get_runtime)) -> EstimateBudgetOutput:
    out = rt.orchestrator_v1.registry.dispatch("estimate_budget", req.model_dump())
    return EstimateBudgetOutput.model_validate(out)

