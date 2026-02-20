"""DiagnosticComControlSubNodeChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticComControlSubNodeChannel(ARObject):
    """AUTOSAR DiagnosticComControlSubNodeChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sub_node: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlSubNodeChannel."""
        super().__init__()
        self.sub_node: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlSubNodeChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sub_node
        if self.sub_node is not None:
            serialized = ARObject._serialize_item(self.sub_node, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB-NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSubNodeChannel":
        """Deserialize XML element to DiagnosticComControlSubNodeChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlSubNodeChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sub_node
        child = ARObject._find_child_element(element, "SUB-NODE")
        if child is not None:
            sub_node_value = child.text
            obj.sub_node = sub_node_value

        return obj



class DiagnosticComControlSubNodeChannelBuilder:
    """Builder for DiagnosticComControlSubNodeChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlSubNodeChannel = DiagnosticComControlSubNodeChannel()

    def build(self) -> DiagnosticComControlSubNodeChannel:
        """Build and return DiagnosticComControlSubNodeChannel object.

        Returns:
            DiagnosticComControlSubNodeChannel instance
        """
        # TODO: Add validation
        return self._obj
