"""DiagnosticJ1939ExpandedFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)


class DiagnosticJ1939ExpandedFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939ExpandedFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    node: Optional[DiagnosticJ1939Node]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939ExpandedFreezeFrame."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939ExpandedFreezeFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939ExpandedFreezeFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize node
        if self.node is not None:
            serialized = ARObject._serialize_item(self.node, "DiagnosticJ1939Node")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939ExpandedFreezeFrame":
        """Deserialize XML element to DiagnosticJ1939ExpandedFreezeFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939ExpandedFreezeFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939ExpandedFreezeFrame, cls).deserialize(element)

        # Parse node
        child = ARObject._find_child_element(element, "NODE")
        if child is not None:
            node_value = ARObject._deserialize_by_tag(child, "DiagnosticJ1939Node")
            obj.node = node_value

        return obj



class DiagnosticJ1939ExpandedFreezeFrameBuilder:
    """Builder for DiagnosticJ1939ExpandedFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939ExpandedFreezeFrame = DiagnosticJ1939ExpandedFreezeFrame()

    def build(self) -> DiagnosticJ1939ExpandedFreezeFrame:
        """Build and return DiagnosticJ1939ExpandedFreezeFrame object.

        Returns:
            DiagnosticJ1939ExpandedFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
