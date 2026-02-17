"""TransmissionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2075)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TransmissionComSpecProps(ARObject):
    """AUTOSAR TransmissionComSpecProps."""

    data_update: Optional[TimeValue]
    minimum_send: Optional[TimeValue]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransmissionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.minimum_send: Optional[TimeValue] = None
        self.transmission: Optional[Any] = None


class TransmissionComSpecPropsBuilder:
    """Builder for TransmissionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionComSpecProps = TransmissionComSpecProps()

    def build(self) -> TransmissionComSpecProps:
        """Build and return TransmissionComSpecProps object.

        Returns:
            TransmissionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
