"""HwDescriptionEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 15)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 990)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
    HwAttributeValue,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
    HwCategory,
)

if TYPE_CHECKING:
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
    _hw_categorie_refs: list[ARRef]
    hw_type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize HwDescriptionEntity."""
        super().__init__()
        self.hw_attributes: list[HwAttributeValue] = []
        self._hw_categorie_refs: list[ARRef] = []
        self.hw_type_ref: Optional[ARRef] = None
    @property
    @xml_element_name("HW-CATEGORYS")
    def hw_categorie_refs(self) -> list[ARRef]:
        """Get hw_categorie_refs with custom XML element name."""
        return self._hw_categorie_refs

    @hw_categorie_refs.setter
    def hw_categorie_refs(self, value: list[ARRef]) -> None:
        """Set hw_categorie_refs with custom XML element name."""
        self._hw_categorie_refs = value


    def serialize(self) -> ET.Element:
        """Serialize HwDescriptionEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwDescriptionEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_attributes (list to container "HW-ATTRIBUTES")
        if self.hw_attributes:
            wrapper = ET.Element("HW-ATTRIBUTES")
            for item in self.hw_attributes:
                serialized = SerializationHelper.serialize_item(item, "HwAttributeValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_categorie_refs (list to container "HW-CATEGORYS")
        if self.hw_categorie_refs:
            wrapper = ET.Element("HW-CATEGORYS")
            for item in self.hw_categorie_refs:
                serialized = SerializationHelper.serialize_item(item, "HwCategory")
                if serialized is not None:
                    child_elem = ET.Element("HW-CATEGORIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_type_ref
        if self.hw_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_type_ref, "HwType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-TYPE-REF")
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
        container = SerializationHelper.find_child_element(element, "HW-ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_attributes.append(child_value)

        # Parse hw_categorie_refs (list from container "HW-CATEGORYS")
        obj.hw_categorie_refs = []
        container = SerializationHelper.find_child_element(element, "HW-CATEGORYS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_categorie_refs.append(child_value)

        # Parse hw_type_ref
        child = SerializationHelper.find_child_element(element, "HW-TYPE-REF")
        if child is not None:
            hw_type_ref_value = ARRef.deserialize(child)
            obj.hw_type_ref = hw_type_ref_value

        return obj



