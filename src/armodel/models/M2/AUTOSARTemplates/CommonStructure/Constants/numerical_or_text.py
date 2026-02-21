"""NumericalOrText AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    String,
)


class NumericalOrText(ARObject):
    """AUTOSAR NumericalOrText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    vf: Optional[Numerical]
    vt: Optional[String]
    def __init__(self) -> None:
        """Initialize NumericalOrText."""
        super().__init__()
        self.vf: Optional[Numerical] = None
        self.vt: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize NumericalOrText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NumericalOrText, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize vf
        if self.vf is not None:
            serialized = SerializationHelper.serialize_item(self.vf, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vt
        if self.vt is not None:
            serialized = SerializationHelper.serialize_item(self.vt, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalOrText":
        """Deserialize XML element to NumericalOrText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NumericalOrText object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NumericalOrText, cls).deserialize(element)

        # Parse vf
        child = SerializationHelper.find_child_element(element, "VF")
        if child is not None:
            vf_value = child.text
            obj.vf = vf_value

        # Parse vt
        child = SerializationHelper.find_child_element(element, "VT")
        if child is not None:
            vt_value = child.text
            obj.vt = vt_value

        return obj



class NumericalOrTextBuilder:
    """Builder for NumericalOrText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalOrText = NumericalOrText()

    def build(self) -> NumericalOrText:
        """Build and return NumericalOrText object.

        Returns:
            NumericalOrText instance
        """
        # TODO: Add validation
        return self._obj
