"""PhysConstrs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 406)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MonotonyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.scale_constr import (
    ScaleConstr,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class PhysConstrs(ARObject):
    """AUTOSAR PhysConstrs."""

    lower_limit: Optional[Limit]
    max_diff: Optional[Numerical]
    max_gradient: Optional[Numerical]
    monotony: Optional[MonotonyEnum]
    scale_constrs: list[ScaleConstr]
    unit: Optional[Unit]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize PhysConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.unit: Optional[Unit] = None
        self.upper_limit: Optional[Limit] = None


class PhysConstrsBuilder:
    """Builder for PhysConstrs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysConstrs = PhysConstrs()

    def build(self) -> PhysConstrs:
        """Build and return PhysConstrs object.

        Returns:
            PhysConstrs instance
        """
        # TODO: Add validation
        return self._obj
