"""ISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ISignalProps(ARObject):
    """AUTOSAR ISignalProps."""

    handle_out_of_range: Optional[Any]
    def __init__(self) -> None:
        """Initialize ISignalProps."""
        super().__init__()
        self.handle_out_of_range: Optional[Any] = None


class ISignalPropsBuilder:
    """Builder for ISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalProps = ISignalProps()

    def build(self) -> ISignalProps:
        """Build and return ISignalProps object.

        Returns:
            ISignalProps instance
        """
        # TODO: Add validation
        return self._obj
