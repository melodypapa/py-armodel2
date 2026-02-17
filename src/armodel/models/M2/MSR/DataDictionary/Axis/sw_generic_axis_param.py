"""SwGenericAxisParam AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 356)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SwGenericAxisParam(ARObject):
    """AUTOSAR SwGenericAxisParam."""

    def __init__(self) -> None:
        """Initialize SwGenericAxisParam."""
        super().__init__()
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None


class SwGenericAxisParamBuilder:
    """Builder for SwGenericAxisParam."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParam = SwGenericAxisParam()

    def build(self) -> SwGenericAxisParam:
        """Build and return SwGenericAxisParam object.

        Returns:
            SwGenericAxisParam instance
        """
        # TODO: Add validation
        return self._obj
