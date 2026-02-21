"""DiagnosticTestIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestIdentifier(ARObject):
    """AUTOSAR DiagnosticTestIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    uas_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTestIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.uas_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTestIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uas_id
        if self.uas_id is not None:
            serialized = SerializationHelper.serialize_item(self.uas_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UAS-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestIdentifier":
        """Deserialize XML element to DiagnosticTestIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse uas_id
        child = SerializationHelper.find_child_element(element, "UAS-ID")
        if child is not None:
            uas_id_value = child.text
            obj.uas_id = uas_id_value

        return obj



class DiagnosticTestIdentifierBuilder:
    """Builder for DiagnosticTestIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestIdentifier = DiagnosticTestIdentifier()

    def build(self) -> DiagnosticTestIdentifier:
        """Build and return DiagnosticTestIdentifier object.

        Returns:
            DiagnosticTestIdentifier instance
        """
        # TODO: Add validation
        return self._obj
