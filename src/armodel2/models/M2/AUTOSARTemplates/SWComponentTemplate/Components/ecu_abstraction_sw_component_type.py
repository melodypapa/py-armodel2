"""EcuAbstractionSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 647)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2020)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import AtomicSwComponentTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """AUTOSAR EcuAbstractionSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECU-ABSTRACTION-SW-COMPONENT-TYPE"


    hardware_element_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HARDWARE-ELEMENT-REFS": ("_POLYMORPHIC_LIST", "hardware_element_refs", ["HwElement", "HwPin", "HwPinGroup", "HwType"]),
    }


    def __init__(self) -> None:
        """Initialize EcuAbstractionSwComponentType."""
        super().__init__()
        self.hardware_element_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcuAbstractionSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuAbstractionSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hardware_element_refs (list to container "HARDWARE-ELEMENT-REFS")
        if self.hardware_element_refs:
            wrapper = ET.Element("HARDWARE-ELEMENT-REFS")
            for item in self.hardware_element_refs:
                serialized = SerializationHelper.serialize_item(item, "HwDescriptionEntity")
                if serialized is not None:
                    child_elem = ET.Element("HARDWARE-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuAbstractionSwComponentType":
        """Deserialize XML element to EcuAbstractionSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuAbstractionSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuAbstractionSwComponentType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HARDWARE-ELEMENT-REFS":
                for item_elem in child:
                    obj.hardware_element_refs.append(ARRef.deserialize(item_elem))

        return obj



class EcuAbstractionSwComponentTypeBuilder(AtomicSwComponentTypeBuilder):
    """Builder for EcuAbstractionSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcuAbstractionSwComponentType = EcuAbstractionSwComponentType()


    def with_hardware_elements(self, items: list[HwDescriptionEntity]) -> "EcuAbstractionSwComponentTypeBuilder":
        """Set hardware_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hardware_elements = list(items) if items else []
        return self


    def add_hardware_element(self, item: HwDescriptionEntity) -> "EcuAbstractionSwComponentTypeBuilder":
        """Add a single item to hardware_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hardware_elements.append(item)
        return self

    def clear_hardware_elements(self) -> "EcuAbstractionSwComponentTypeBuilder":
        """Clear all items from hardware_elements list.

        Returns:
            self for method chaining
        """
        self._obj.hardware_elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "hardwareElement",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcuAbstractionSwComponentType:
        """Build and return the EcuAbstractionSwComponentType instance with validation."""
        self._validate_instance()
        return self._obj