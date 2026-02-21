"""EcucAbstractConfigurationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucConfigurationClassEnum,
)
from abc import ABC, abstractmethod


class EcucAbstractConfigurationClass(ARObject, ABC):
    """AUTOSAR EcucAbstractConfigurationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    config_class: Optional[EcucConfigurationClassEnum]
    config_variant: Optional[Any]
    def __init__(self) -> None:
        """Initialize EcucAbstractConfigurationClass."""
        super().__init__()
        self.config_class: Optional[EcucConfigurationClassEnum] = None
        self.config_variant: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAbstractConfigurationClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAbstractConfigurationClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize config_class
        if self.config_class is not None:
            serialized = SerializationHelper.serialize_item(self.config_class, "EcucConfigurationClassEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize config_variant
        if self.config_variant is not None:
            serialized = SerializationHelper.serialize_item(self.config_variant, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractConfigurationClass":
        """Deserialize XML element to EcucAbstractConfigurationClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractConfigurationClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAbstractConfigurationClass, cls).deserialize(element)

        # Parse config_class
        child = SerializationHelper.find_child_element(element, "CONFIG-CLASS")
        if child is not None:
            config_class_value = EcucConfigurationClassEnum.deserialize(child)
            obj.config_class = config_class_value

        # Parse config_variant
        child = SerializationHelper.find_child_element(element, "CONFIG-VARIANT")
        if child is not None:
            config_variant_value = child.text
            obj.config_variant = config_variant_value

        return obj



class EcucAbstractConfigurationClassBuilder:
    """Builder for EcucAbstractConfigurationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractConfigurationClass = EcucAbstractConfigurationClass()

    def build(self) -> EcucAbstractConfigurationClass:
        """Build and return EcucAbstractConfigurationClass object.

        Returns:
            EcucAbstractConfigurationClass instance
        """
        # TODO: Add validation
        return self._obj
