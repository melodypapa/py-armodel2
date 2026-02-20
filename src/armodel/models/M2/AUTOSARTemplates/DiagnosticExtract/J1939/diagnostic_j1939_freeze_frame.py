"""DiagnosticJ1939FreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 220)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)


class DiagnosticJ1939FreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939FreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    node_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939FreezeFrame."""
        super().__init__()
        self.node_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939FreezeFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939FreezeFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize node_ref
        if self.node_ref is not None:
            serialized = ARObject._serialize_item(self.node_ref, "DiagnosticJ1939Node")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939FreezeFrame":
        """Deserialize XML element to DiagnosticJ1939FreezeFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939FreezeFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939FreezeFrame, cls).deserialize(element)

        # Parse node_ref
        child = ARObject._find_child_element(element, "NODE-REF")
        if child is not None:
            node_ref_value = ARRef.deserialize(child)
            obj.node_ref = node_ref_value

        return obj



class DiagnosticJ1939FreezeFrameBuilder:
    """Builder for DiagnosticJ1939FreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939FreezeFrame = DiagnosticJ1939FreezeFrame()

    def build(self) -> DiagnosticJ1939FreezeFrame:
        """Build and return DiagnosticJ1939FreezeFrame object.

        Returns:
            DiagnosticJ1939FreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
