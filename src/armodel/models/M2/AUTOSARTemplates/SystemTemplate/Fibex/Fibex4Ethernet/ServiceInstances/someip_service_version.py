"""SomeipServiceVersion AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2059)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SomeipServiceVersion(ARObject):
    """AUTOSAR SomeipServiceVersion."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    major_version: Optional[PositiveInteger]
    minor_version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipServiceVersion."""
        super().__init__()
        self.major_version: Optional[PositiveInteger] = None
        self.minor_version: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SomeipServiceVersion to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize major_version
        if self.major_version is not None:
            serialized = ARObject._serialize_item(self.major_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAJOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = ARObject._serialize_item(self.minor_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipServiceVersion":
        """Deserialize XML element to SomeipServiceVersion object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipServiceVersion object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse major_version
        child = ARObject._find_child_element(element, "MAJOR-VERSION")
        if child is not None:
            major_version_value = child.text
            obj.major_version = major_version_value

        # Parse minor_version
        child = ARObject._find_child_element(element, "MINOR-VERSION")
        if child is not None:
            minor_version_value = child.text
            obj.minor_version = minor_version_value

        return obj



class SomeipServiceVersionBuilder:
    """Builder for SomeipServiceVersion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipServiceVersion = SomeipServiceVersion()

    def build(self) -> SomeipServiceVersion:
        """Build and return SomeipServiceVersion object.

        Returns:
            SomeipServiceVersion instance
        """
        # TODO: Add validation
        return self._obj
