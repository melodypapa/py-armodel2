"""CanXlFrameTriggeringProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanXlFrameTriggeringProps(ARObject):
    """AUTOSAR CanXlFrameTriggeringProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acceptance_field: Optional[PositiveInteger]
    priority_id: Optional[PositiveInteger]
    sdu_type: Optional[PositiveInteger]
    vcid: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanXlFrameTriggeringProps."""
        super().__init__()
        self.acceptance_field: Optional[PositiveInteger] = None
        self.priority_id: Optional[PositiveInteger] = None
        self.sdu_type: Optional[PositiveInteger] = None
        self.vcid: Optional[PositiveInteger] = None


class CanXlFrameTriggeringPropsBuilder:
    """Builder for CanXlFrameTriggeringProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanXlFrameTriggeringProps = CanXlFrameTriggeringProps()

    def build(self) -> CanXlFrameTriggeringProps:
        """Build and return CanXlFrameTriggeringProps object.

        Returns:
            CanXlFrameTriggeringProps instance
        """
        # TODO: Add validation
        return self._obj
