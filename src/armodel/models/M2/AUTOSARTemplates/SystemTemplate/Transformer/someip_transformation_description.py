"""SOMEIPTransformationDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 777)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationDescription(TransformationDescription):
    """AUTOSAR SOMEIPTransformationDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[PositiveInteger]
    byte_order: Optional[ByteOrderEnum]
    interface_version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SOMEIPTransformationDescription."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.interface_version: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SOMEIPTransformationDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SOMEIPTransformationDescription, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = ARObject._serialize_item(self.alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize byte_order
        if self.byte_order is not None:
            serialized = ARObject._serialize_item(self.byte_order, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize interface_version
        if self.interface_version is not None:
            serialized = ARObject._serialize_item(self.interface_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERFACE-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationDescription":
        """Deserialize XML element to SOMEIPTransformationDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SOMEIPTransformationDescription, cls).deserialize(element)

        # Parse alignment
        child = ARObject._find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse byte_order
        child = ARObject._find_child_element(element, "BYTE-ORDER")
        if child is not None:
            byte_order_value = ByteOrderEnum.deserialize(child)
            obj.byte_order = byte_order_value

        # Parse interface_version
        child = ARObject._find_child_element(element, "INTERFACE-VERSION")
        if child is not None:
            interface_version_value = child.text
            obj.interface_version = interface_version_value

        return obj



class SOMEIPTransformationDescriptionBuilder:
    """Builder for SOMEIPTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationDescription = SOMEIPTransformationDescription()

    def build(self) -> SOMEIPTransformationDescription:
        """Build and return SOMEIPTransformationDescription object.

        Returns:
            SOMEIPTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
