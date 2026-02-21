"""DiagnosticIumprGroupIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class DiagnosticIumprGroupIdentifier(ARObject):
    """AUTOSAR DiagnosticIumprGroupIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    group_id: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroupIdentifier."""
        super().__init__()
        self.group_id: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIumprGroupIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIumprGroupIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize group_id
        if self.group_id is not None:
            serialized = SerializationHelper.serialize_item(self.group_id, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GROUP-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprGroupIdentifier":
        """Deserialize XML element to DiagnosticIumprGroupIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprGroupIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumprGroupIdentifier, cls).deserialize(element)

        # Parse group_id
        child = SerializationHelper.find_child_element(element, "GROUP-ID")
        if child is not None:
            group_id_value = child.text
            obj.group_id = group_id_value

        return obj



class DiagnosticIumprGroupIdentifierBuilder:
    """Builder for DiagnosticIumprGroupIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprGroupIdentifier = DiagnosticIumprGroupIdentifier()

    def build(self) -> DiagnosticIumprGroupIdentifier:
        """Build and return DiagnosticIumprGroupIdentifier object.

        Returns:
            DiagnosticIumprGroupIdentifier instance
        """
        # TODO: Add validation
        return self._obj
