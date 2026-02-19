"""FlexrayNmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class FlexrayNmEcu(BusspecificNmEcu):
    """AUTOSAR FlexrayNmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_hw_vote: Optional[Boolean]
    nm_main: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize FlexrayNmEcu."""
        super().__init__()
        self.nm_hw_vote: Optional[Boolean] = None
        self.nm_main: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmEcu":
        """Deserialize XML element to FlexrayNmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayNmEcu, cls).deserialize(element)

        # Parse nm_hw_vote
        child = ARObject._find_child_element(element, "NM-HW-VOTE")
        if child is not None:
            nm_hw_vote_value = child.text
            obj.nm_hw_vote = nm_hw_vote_value

        # Parse nm_main
        child = ARObject._find_child_element(element, "NM-MAIN")
        if child is not None:
            nm_main_value = child.text
            obj.nm_main = nm_main_value

        return obj



class FlexrayNmEcuBuilder:
    """Builder for FlexrayNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmEcu = FlexrayNmEcu()

    def build(self) -> FlexrayNmEcu:
        """Build and return FlexrayNmEcu object.

        Returns:
            FlexrayNmEcu instance
        """
        # TODO: Add validation
        return self._obj
