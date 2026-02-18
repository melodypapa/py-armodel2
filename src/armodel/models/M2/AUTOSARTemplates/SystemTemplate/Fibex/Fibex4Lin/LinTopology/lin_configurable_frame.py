"""LinConfigurableFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinConfigurableFrame(ARObject):
    """AUTOSAR LinConfigurableFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame: Optional[LinFrame]
    message_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinConfigurableFrame."""
        super().__init__()
        self.frame: Optional[LinFrame] = None
        self.message_id: Optional[PositiveInteger] = None


class LinConfigurableFrameBuilder:
    """Builder for LinConfigurableFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinConfigurableFrame = LinConfigurableFrame()

    def build(self) -> LinConfigurableFrame:
        """Build and return LinConfigurableFrame object.

        Returns:
            LinConfigurableFrame instance
        """
        # TODO: Add validation
        return self._obj
