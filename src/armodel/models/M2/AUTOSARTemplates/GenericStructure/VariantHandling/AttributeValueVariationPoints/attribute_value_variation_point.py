"""AttributeValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 617)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 209)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
    String,
)
from abc import ABC, abstractmethod


class AttributeValueVariationPoint(ARObject, ABC):
    """AUTOSAR AttributeValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    binding_time_enum: Optional[BindingTimeEnum]
    blueprint_value: Optional[String]
    sd: Optional[String]
    short_label: Optional[PrimitiveIdentifier]
    def __init__(self) -> None:
        """Initialize AttributeValueVariationPoint."""
        super().__init__()
        self.binding_time_enum: Optional[BindingTimeEnum] = None
        self.blueprint_value: Optional[String] = None
        self.sd: Optional[String] = None
        self.short_label: Optional[PrimitiveIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize AttributeValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AttributeValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize binding_time_enum
        if self.binding_time_enum is not None:
            serialized = SerializationHelper.serialize_item(self.binding_time_enum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BINDING-TIME-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize blueprint_value
        if self.blueprint_value is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint_value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd
        if self.sd is not None:
            serialized = SerializationHelper.serialize_item(self.sd, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "PrimitiveIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeValueVariationPoint":
        """Deserialize XML element to AttributeValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AttributeValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AttributeValueVariationPoint, cls).deserialize(element)

        # Parse binding_time_enum
        child = SerializationHelper.find_child_element(element, "BINDING-TIME-ENUM")
        if child is not None:
            binding_time_enum_value = BindingTimeEnum.deserialize(child)
            obj.binding_time_enum = binding_time_enum_value

        # Parse blueprint_value
        child = SerializationHelper.find_child_element(element, "BLUEPRINT-VALUE")
        if child is not None:
            blueprint_value_value = child.text
            obj.blueprint_value = blueprint_value_value

        # Parse sd
        child = SerializationHelper.find_child_element(element, "SD")
        if child is not None:
            sd_value = child.text
            obj.sd = sd_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class AttributeValueVariationPointBuilder:
    """Builder for AttributeValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeValueVariationPoint = AttributeValueVariationPoint()

    def build(self) -> AttributeValueVariationPoint:
        """Build and return AttributeValueVariationPoint object.

        Returns:
            AttributeValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
