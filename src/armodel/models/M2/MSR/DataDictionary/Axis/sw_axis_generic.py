"""SwAxisGeneric AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
    SwAxisType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisGeneric(ARObject):
    """AUTOSAR SwAxisGeneric."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_axis_type: Optional[SwAxisType]
    sw_generic_axis_params: list[SwGenericAxisParam]
    def __init__(self) -> None:
        """Initialize SwAxisGeneric."""
        super().__init__()
        self.sw_axis_type: Optional[SwAxisType] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []


class SwAxisGenericBuilder:
    """Builder for SwAxisGeneric."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGeneric = SwAxisGeneric()

    def build(self) -> SwAxisGeneric:
        """Build and return SwAxisGeneric object.

        Returns:
            SwAxisGeneric instance
        """
        # TODO: Add validation
        return self._obj
