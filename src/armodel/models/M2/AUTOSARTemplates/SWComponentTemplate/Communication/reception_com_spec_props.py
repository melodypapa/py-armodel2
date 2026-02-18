"""ReceptionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class ReceptionComSpecProps(ARObject):
    """AUTOSAR ReceptionComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_update: Optional[TimeValue]
    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ReceptionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.timeout: Optional[TimeValue] = None


class ReceptionComSpecPropsBuilder:
    """Builder for ReceptionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceptionComSpecProps = ReceptionComSpecProps()

    def build(self) -> ReceptionComSpecProps:
        """Build and return ReceptionComSpecProps object.

        Returns:
            ReceptionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
