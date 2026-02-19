"""FlexrayNmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FlexrayNmNode(NmNode):
    """AUTOSAR FlexrayNmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize FlexrayNmNode."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmNode":
        """Deserialize XML element to FlexrayNmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmNode object
        """
        # Delegate to parent class to handle inherited attributes
        return super(FlexrayNmNode, cls).deserialize(element)



class FlexrayNmNodeBuilder:
    """Builder for FlexrayNmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmNode = FlexrayNmNode()

    def build(self) -> FlexrayNmNode:
        """Build and return FlexrayNmNode object.

        Returns:
            FlexrayNmNode instance
        """
        # TODO: Add validation
        return self._obj
