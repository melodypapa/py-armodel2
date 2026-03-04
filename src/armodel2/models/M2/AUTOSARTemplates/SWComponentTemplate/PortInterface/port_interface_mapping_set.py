"""PortInterfaceMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 119)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PortInterfaceMappingSet(ARElement):
    """AUTOSAR PortInterfaceMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PORT-INTERFACE-MAPPING-SET"


    port_interface_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PORT-INTERFACE-REFS": ("_POLYMORPHIC_LIST", "port_interface_refs", ["ClientServerInterfaceMapping", "ModeInterfaceMapping", "TriggerInterfaceMapping", "VariableAndParameter"]),
    }


    def __init__(self) -> None:
        """Initialize PortInterfaceMappingSet."""
        super().__init__()
        self.port_interface_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PortInterfaceMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortInterfaceMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_interface_refs (list to container "PORT-INTERFACE-REFS")
        if self.port_interface_refs:
            wrapper = ET.Element("PORT-INTERFACE-REFS")
            for item in self.port_interface_refs:
                serialized = SerializationHelper.serialize_item(item, "PortInterfaceMapping")
                if serialized is not None:
                    child_elem = ET.Element("PORT-INTERFACE-REF")
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
    def deserialize(cls, element: ET.Element) -> "PortInterfaceMappingSet":
        """Deserialize XML element to PortInterfaceMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortInterfaceMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortInterfaceMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PORT-INTERFACE-REFS":
                for item_elem in child:
                    obj.port_interface_refs.append(ARRef.deserialize(item_elem))

        return obj



class PortInterfaceMappingSetBuilder(ARElementBuilder):
    """Builder for PortInterfaceMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortInterfaceMappingSet = PortInterfaceMappingSet()


    def with_port_interfaces(self, items: list[PortInterfaceMapping]) -> "PortInterfaceMappingSetBuilder":
        """Set port_interfaces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_interfaces = list(items) if items else []
        return self


    def add_port_interface(self, item: PortInterfaceMapping) -> "PortInterfaceMappingSetBuilder":
        """Add a single item to port_interfaces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_interfaces.append(item)
        return self

    def clear_port_interfaces(self) -> "PortInterfaceMappingSetBuilder":
        """Clear all items from port_interfaces list.

        Returns:
            self for method chaining
        """
        self._obj.port_interfaces = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "portInterface",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PortInterfaceMappingSet:
        """Build and return the PortInterfaceMappingSet instance with validation."""
        self._validate_instance()
        return self._obj