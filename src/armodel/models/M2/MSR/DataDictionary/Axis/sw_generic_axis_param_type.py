"""SwGenericAxisParamType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 356)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)


class SwGenericAxisParamType(Identifiable):
    """AUTOSAR SwGenericAxisParamType."""

    data_constr: Optional[DataConstr]
    def __init__(self) -> None:
        """Initialize SwGenericAxisParamType."""
        super().__init__()
        self.data_constr: Optional[DataConstr] = None


class SwGenericAxisParamTypeBuilder:
    """Builder for SwGenericAxisParamType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParamType = SwGenericAxisParamType()

    def build(self) -> SwGenericAxisParamType:
        """Build and return SwGenericAxisParamType object.

        Returns:
            SwGenericAxisParamType instance
        """
        # TODO: Add validation
        return self._obj
