"""Sdf AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 92)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Numerical,
)


class Sdf(ARObject):
    """AUTOSAR Sdf."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    gid: NameToken
    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize Sdf."""
        super().__init__()
        self.gid: NameToken = None
        self.value: Optional[Numerical] = None
    def serialize(self) -> ET.Element:
        """Serialize Sdf to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize gid
        if self.gid is not None:
            serialized = ARObject._serialize_item(self.gid, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdf":
        """Deserialize XML element to Sdf object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sdf object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse gid
        child = ARObject._find_child_element(element, "GID")
        if child is not None:
            gid_value = child.text
            obj.gid = gid_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class SdfBuilder:
    """Builder for Sdf."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdf = Sdf()

    def build(self) -> Sdf:
        """Build and return Sdf object.

        Returns:
            Sdf instance
        """
        # TODO: Add validation
        return self._obj
