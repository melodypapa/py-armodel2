"""AbstractEnumerationValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Ref,
)
from abc import ABC, abstractmethod


class AbstractEnumerationValueVariationPoint(ARObject, ABC):
    """AUTOSAR AbstractEnumerationValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[Identifier]
    enum_table_ref: Optional[Ref]
    def __init__(self) -> None:
        """Initialize AbstractEnumerationValueVariationPoint."""
        super().__init__()
        self.base: Optional[Identifier] = None
        self.enum_table_ref: Optional[Ref] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractEnumerationValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractEnumerationValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base
        if self.base is not None:
            serialized = SerializationHelper.serialize_item(self.base, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize enum_table_ref
        if self.enum_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.enum_table_ref, "Ref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENUM-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEnumerationValueVariationPoint":
        """Deserialize XML element to AbstractEnumerationValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEnumerationValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractEnumerationValueVariationPoint, cls).deserialize(element)

        # Parse base
        child = SerializationHelper.find_child_element(element, "BASE")
        if child is not None:
            base_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.base = base_value

        # Parse enum_table_ref
        child = SerializationHelper.find_child_element(element, "ENUM-TABLE-REF")
        if child is not None:
            enum_table_ref_value = ARRef.deserialize(child)
            obj.enum_table_ref = enum_table_ref_value

        return obj



