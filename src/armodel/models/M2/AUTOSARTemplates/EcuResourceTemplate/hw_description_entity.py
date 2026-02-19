"""HwDescriptionEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 15)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 990)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
    HwAttributeValue,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
    HwCategory,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_type import (
    HwType,
)
from abc import ABC, abstractmethod


class HwDescriptionEntity(Referrable, ABC):
    """AUTOSAR HwDescriptionEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    hw_attributes: list[HwAttributeValue]
    hw_categories: list[HwCategory]
    hw_type: Optional[HwType]
    def __init__(self) -> None:
        """Initialize HwDescriptionEntity."""
        super().__init__()
        self.hw_attributes: list[HwAttributeValue] = []
        self.hw_categories: list[HwCategory] = []
        self.hw_type: Optional[HwType] = None
    def serialize(self) -> ET.Element:
        """Serialize HwDescriptionEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwDescriptionEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_attributes (list to container "HW-ATTRIBUTES")
        if self.hw_attributes:
            wrapper = ET.Element("HW-ATTRIBUTES")
            for item in self.hw_attributes:
                serialized = ARObject._serialize_item(item, "HwAttributeValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_categories (list to container "HW-CATEGORIES")
        if self.hw_categories:
            wrapper = ET.Element("HW-CATEGORIES")
            for item in self.hw_categories:
                serialized = ARObject._serialize_item(item, "HwCategory")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_type
        if self.hw_type is not None:
            serialized = ARObject._serialize_item(self.hw_type, "HwType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwDescriptionEntity":
        """Deserialize XML element to HwDescriptionEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwDescriptionEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwDescriptionEntity, cls).deserialize(element)

        # Parse hw_attributes (list from container "HW-ATTRIBUTES")
        obj.hw_attributes = []
        container = ARObject._find_child_element(element, "HW-ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_attributes.append(child_value)

        # Parse hw_categories (list from container "HW-CATEGORIES")
        obj.hw_categories = []
        container = ARObject._find_child_element(element, "HW-CATEGORIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_categories.append(child_value)

        # Parse hw_type
        child = ARObject._find_child_element(element, "HW-TYPE")
        if child is not None:
            hw_type_value = ARObject._deserialize_by_tag(child, "HwType")
            obj.hw_type = hw_type_value

        return obj



class HwDescriptionEntityBuilder:
    """Builder for HwDescriptionEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwDescriptionEntity = HwDescriptionEntity()

    def build(self) -> HwDescriptionEntity:
        """Build and return HwDescriptionEntity object.

        Returns:
            HwDescriptionEntity instance
        """
        # TODO: Add validation
        return self._obj
