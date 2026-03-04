"""TriggerInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import PortInterfaceMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger_mapping import (
    TriggerMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TriggerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR TriggerInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRIGGER-INTERFACE-MAPPING"


    trigger_mapping_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TRIGGER-MAPPING-REFS": lambda obj, elem: [obj.trigger_mapping_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize TriggerInterfaceMapping."""
        super().__init__()
        self.trigger_mapping_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize TriggerInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TriggerInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize trigger_mapping_refs (list to container "TRIGGER-MAPPING-REFS")
        if self.trigger_mapping_refs:
            wrapper = ET.Element("TRIGGER-MAPPING-REFS")
            for item in self.trigger_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "TriggerMapping")
                if serialized is not None:
                    child_elem = ET.Element("TRIGGER-MAPPING-REF")
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
    def deserialize(cls, element: ET.Element) -> "TriggerInterfaceMapping":
        """Deserialize XML element to TriggerInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TriggerInterfaceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TRIGGER-MAPPING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.trigger_mapping_refs.append(ARRef.deserialize(item_elem))

        return obj



class TriggerInterfaceMappingBuilder(PortInterfaceMappingBuilder):
    """Builder for TriggerInterfaceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TriggerInterfaceMapping = TriggerInterfaceMapping()


    def with_trigger_mappings(self, items: list[TriggerMapping]) -> "TriggerInterfaceMappingBuilder":
        """Set trigger_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_mappings = list(items) if items else []
        return self


    def add_trigger_mapping(self, item: TriggerMapping) -> "TriggerInterfaceMappingBuilder":
        """Add a single item to trigger_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_mappings.append(item)
        return self

    def clear_trigger_mappings(self) -> "TriggerInterfaceMappingBuilder":
        """Clear all items from trigger_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_mappings = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "triggerMapping",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TriggerInterfaceMapping:
        """Build and return the TriggerInterfaceMapping instance with validation."""
        self._validate_instance()
        return self._obj